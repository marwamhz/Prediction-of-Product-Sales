# Prediction-of-Product-Sales
This project is a sales prediction for food items sold at various stores. The goal of this is to help the retailer understand the properties of products and outlets that play crucial roles in increasing sales.

## Data source 
This is the [data](https://drive.google.com/file/d/1syH81TVrbBsdymLT_jl2JIf6IjPXtSQw/view?usp=sharing) we used here. *(Note: [original data source](https://datahack.analyticsvidhya.com/contest/practice-problem-big-mart-sales-iii/))*
## Data Dictionary

![data_dict](https://github.com/marwamhz/Prediction-of-Product-Sales/assets/160395937/72f46a4f-93b6-44a3-9903-8b85f081ecab)

## Methods
After cleaning data, the following steps were performed:
### Exploratory Data Analysis 
Here we created exploratory visuals to help us understand and explain our data. This includes:
- Histograms to view the distributions of numerical features in the dataset.
- Boxplots to view statistical summaries of numerical features in the dataset.
- Countplots to view the frequency of each class of categorial features in the dataset.
- Heatmap to view the correlation between features.

---
![heatmap](https://github.com/marwamhz/Prediction-of-Product-Sales/assets/160395937/0c7289db-df18-4c67-8205-4bd45e8d9acf)

The heat map shows that there is a positive correlation between the Sales of the product in the particular store (Item_outlet_Sales) and the Maximum Retail Price of the product(Item_MRP). This correlation is moderate.

---
### Explanatory Data Analysis 

![téléchargement (4)](https://github.com/marwamhz/Prediction-of-Product-Sales/assets/160395937/5358a392-4a18-400d-9e08-081c31f8ebbb)

This figure shows that the sales are affected by the outlet type.

## Maching Learning 
For modeling, we choose the Random Forest model with tuned max_depth '10', max_features 'None'& n_estimators '200'. This model explain 58,9% of the variance.
