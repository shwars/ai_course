## Lab: Classification
## Churn Prediction

In this lab we will consider a typical problem of **Churn Prediction**. We will use [Credit Card Curtomers](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers) dataset, which you can download [here](../../../data/BankChurnersProcessed.csv).

Dataset has the following fields:

FIELD | VALUE
-----|---------
CLIENTNUM | Unique client ID
Attrition_Flag | Whether the customer has left the bank (churned)
Customer_Age | Age
Gender | Gender
Dependent_count | Number of family dependets
Education_Level | Education Level
Marital_Status | Marital status
Income_Category | Yearly income category
Card_Category | Type of credit card
Months_on_book | How long the customer is with this bank
Total_Relationship_Count | Number of bank products customer has
Months_Inactive_12_mon | Number of inactive months over last year
Contacts_Count_12_mon | Number of contacts over last year
Credit_Limit | Credit limit
Total_Revolving_Bal | Total active balance
Avg_Open_To_Buy | Difference between credit limit and current balance, average over last year 
Total_Amt_Chng_Q4_Q1 | Change in the transaction amount per year (Q4 to Q1)
Total_Trans_Amt | Total amount of transactions per year
Total_Trans_Ct | Total number of transactions per year
Total_Ct_Chng_Q4_Q1 | Change in the number of transactions per year (Q4 to Q1)
Avg_Utilization_Ratio | Total amount of money in the bank divided by credit limit (in %)

You need to predict **Attrition_Flag** for a specific client.

Major milestones:

**Preliminary Data Analysis**

* Check which percentage of data corresponds to churned clients. Is this problem well-balanced? What can we expect as a result or training a model on such data?

> Non-balanced dataset means that the accuracy of the model will not reflect its quality. You need to look at other metrics, such as precision, recall and F1-measure.

* Check to see if the data has any missing values. If so - decide what to do with them.
* Calculate mean values of all features for attrited and non-attrited customers separately, and conclude what affects the attrition flag the most.
* Think about augmenting the dataset with some additional features. Consider average transaction amount (`Total_Trans_Amt`/`Total_Trans_Ct`), and some more.
* To see if the age affects the result, plot histogram of ages separately for attrited and non-attrited clients. You can do the same with any numeric feature as well.

**Vectorization**

* Split the data between training and test dataset
* See which features are categorical, and for those features determine if it is nominal or ordinal.
* Think about dropping some features from the model. Look into correlation between columns to make informed decisions.
* Use `ColumnTransformer` for vectorization of all categorical features.

**Model Training**

* Train several ML classification models using SkLearn (logistic regression, decision tree, SVM) and check all metrics on test dataset: accuracy, precision, recall
* Interpret models where possible and comment on the result.
* [OPTIONAL] Have a look at [CatBoost](https://catboost.ai/) library from Yandex and try to use it for solving the problem. Compare metrics. CatBoost is known to work especially well with categorical features.

