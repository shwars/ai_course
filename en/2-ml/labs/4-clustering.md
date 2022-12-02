## Clustering of Bank Clients

In this lab, we will consider the same [bank clients dataset](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers), as in the last lab. Slightly modified version of the dataset is [here](../../../data/BankChurnersProcessed.csv).

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

You need to see whether clients can be clustered, and whether cluster correspond to churn classes.

### Major Milestones

**Data Cleaning**

Since clustering uses Descartes distance between vectors, we need to convert all features to numeric

> Look at all categorical features and think how they can be encoded as numeric. Remember about nominal and ordinal features.

* Some features have `Unknown` values. Think about how to handle them. For example, you can delete corresponding rows, and consider only clients for whom all features are known. 
* Convert all features into numeric. You can use `LabelEncoder` from Scikit Learn, or do it manually. Keep in mind that you need to keep the right order for ordinal values (eg. Education Levels should be ordered as `Uneducated`, `High School`, `College`, `Graduate`, `Post-Graduate`, `Doctorate`).
* Use `StandardScaler` or `MinMaxScaler` to convert all values to one range

> Do not use `Attrition_Flag` for clustering, because we want to see how clients can be structures regardless of their decision to leave the bank.

**Data Visualization**

* Use PCA to visualize all clients in 2D space. Set color of dots according to `Attrition_Flag`.
* Can you visually notice any clustering?
* How many classes can we spot?

**Clustering**

* Use K-Means clustering to cluster clients into corresponding number of clusters (which you can visually determine at previous step).
* Convert cluster centroids to the scale of original values (using `inverse_transform`), and interpret each cluster according to those values.
* Use inertia vs. number of clusters graph to determine the optimal number of clusters for this task.
* Show those clusters on the scatter plot from the visualization part
* See how well clusters correlate with attrition.


