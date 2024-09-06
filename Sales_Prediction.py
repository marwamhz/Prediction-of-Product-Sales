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