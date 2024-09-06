import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO


# Show title
st.title('Sales Price Analysis')


# Function for loading data
# Adding data caching
@st.cache_data
def load_data():
    fpath =  "Data/sales_predictions_2023_modified.csv"
    df = pd.read_csv(fpath, index_col=False)
    return df

# Function for EDA
def explore_numeric(df, x, figsize=(6,5) ):
  # Making our figure with gridspec for subplots
  gridspec = {'height_ratios':[0.7,0.3]}
  fig, axes = plt.subplots(nrows=2, figsize=figsize, sharex=True, gridspec_kw=gridspec)
  # Histogram on Top
  sns.histplot(data=df, x=x, ax=axes[0])
  # Boxplot on Bottom
  sns.boxplot(data=df, x=x, ax=axes[1])
  ## Adding a title
  axes[0].set_title(f"Column: {x}", fontweight='bold')
  ## Adjusting subplots to best fill Figure
  fig.tight_layout()
  # Ensure plot is shown before message
  plt.show()
  return fig

def explore_categorical(df, x, fillna = True, placeholder = 'MISSING', figsize = (6,4), order = None):
  # Make a copy of the dataframe and fillna 
  temp_df = df.copy()
  # Before filling nulls, save null value counts and percent for printing 
  null_count = temp_df[x].isna().sum()
  null_perc = null_count/len(temp_df)* 100
  # fillna with placeholder
  if fillna == True:
    temp_df[x] = temp_df[x].fillna(placeholder)
  # Create figure with desired figsize
  fig, ax = plt.subplots(figsize=figsize)
  # Plotting a count plot 
  sns.countplot(data=temp_df, x=x, ax=ax, order=order)
  # Rotate Tick Labels for long names
  ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
  # Add a title with the feature name included
  ax.set_title(f"Column: {x}")
  # Fix layout and show plot (before print statements)
  fig.tight_layout()
  plt.show()
  return fig, ax


def plot_categorical_vs_target(df, x, y='Item_Outlet_Sales',figsize=(6,4), fillna = True, placeholder = 'MISSING', order = None):
  # Make a copy of the dataframe and fillna 
  temp_df = df.copy()
  # fillna with placeholder
  if fillna == True:
    temp_df[x] = temp_df[x].fillna(placeholder)
  # or drop nulls prevent unwanted 'nan' group in stripplot
  else:
    temp_df = temp_df.dropna(subset=[x]) 
  # Create the figure and subplots
  fig, ax = plt.subplots(figsize=figsize)
  # Barplot 
  sns.barplot(data=temp_df, x=x, y=y, ax=ax, order=order, alpha=0.6, linewidth=1, edgecolor='black', errorbar=None)
  # Boxplot
  sns.stripplot(data=temp_df, x=x, y=y, hue=x, ax=ax, order=order, hue_order=order, legend=False, edgecolor='white', linewidth=0.5, size=3,zorder=0)
  # Rotate xlabels
  ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
  # Add a title
  ax.set_title(f"{x} vs. {y}")
  fig.tight_layout()
  return fig, ax

def plot_numeric_vs_target(df, x, y='Item_Outlet_Sales', figsize=(6,4), **kwargs): 
  # Calculate the correlation
  corr = df[[x,y]].corr().round(2)
  r = corr.loc[x,y]
  # Plot the data
  fig, ax = plt.subplots(figsize=figsize)
  scatter_kws={'ec':'white','lw':1,'alpha':0.8}
  sns.regplot(data=df, x=x, y=y, ax=ax, scatter_kws=scatter_kws, **kwargs) 
  ## Add the title with the correlation
  ax.set_title(f"{x} vs. {y} (r = {r})")
  # Make sure the plot is shown before the print statement
  plt.show()
  return fig, ax


# load the data 
df = load_data()

# Capture .info()
## Create a string buffer to capture the content
buffer = StringIO()
## Write the info into the buffer
df.info(buf=buffer)
## Retrieve the content from the buffer
summary_info = buffer.getvalue()

# Capture Null Values
# Create a string buffer to capture the content
buffer = StringIO()
## Write the content into the buffer...use to_string
df.isna().sum().to_string(buffer)
## Retrieve the content from the buffer
null_values = buffer.getvalue()



# Display an interactive dataframe
st.markdown('## Product Sales Data')
st.dataframe(df, width=800)

# Display descriptive statistics
st.markdown('### Descriptive Statistics')
if st.button("Show Descriptive Statistics"):
    st.dataframe(df.describe().round(2))

# Display the info
st.markdown("### Summary Info")
if st.button("Show Summary Info"):
    st.text(summary_info)

# Display the Null Values
st.markdown("### Null Values")
if st.button("Show Null Values"):
    st.text(null_values)


st.markdown("## Explore Features")
# Add a selectbox for all possible features
columns = df.columns
column = st.selectbox(label="Select a column", options=columns)
# Conditional statement to determine which function to use
if df[column].dtype == 'object':
    fig, ax  = explore_categorical(df, column)
else:
    fig = explore_numeric(df, column)
# Display appropriate eda plots
st.pyplot(fig)


st.markdown("## Explore Features vs. Item_Outlet_Sales")
# Define target
target = 'Item_Outlet_Sales'
# Remove target from list of features
features_to_use = df.columns[df.columns != target]
# Add a selectbox for all possible columns
feature = st.selectbox(label="Select a feature to compare with Item_Outlet_Sales", options=features_to_use)
# Conditional statement to determine which function to use
if df[feature].dtype == 'object':
    fig, ax  = plot_categorical_vs_target(df, x = feature)
else:
    fig, ax  = plot_numeric_vs_target(df, x = feature)
# Display appropriate eda plots
st.pyplot(fig)