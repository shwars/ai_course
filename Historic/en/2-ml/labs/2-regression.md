## Lab: Regression
## Predicting House Price in SkLearn

In this lab, we will use [King County House Prices Dataset](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction). We have provided [slightly modified dataset](../../../data/kc_house_data_processed.csv) as part of this repo.

Major steps:

#### Data Visualization

* Load the Dataset using Pandas
* Plot the graph of the price vs. different parameters, eg. area of the house (`sqft_living` or `sqft_lot`). Use Scatter Plot
* Use Seaborn to show dependencies between all data columns. [This blog post](https://kgptalkie.medium.com/complete-seaborn-python-tutorial-for-data-visualization-in-python-399af0792ef4) contains a good intro into Seaborn. 
* Observe how average price changes depnding on the availability of a view (`view`), being close to waterfront (`waterfront`) or condition of the house (`condition`). Use `groupby` and aggregation.

#### Train Linear Regression Model

* Do train-test split
* Decide which features you need to use for price prediction.
* Do some data cleaning and pre-processing. Which transformers you need to use and why?
* Train Linear Regression model. What is the accuracy? relative error? 
* Interpret the model using coefficients. Which conclusions you can make?

#### Adding Features

* Try to add some additional features into the model, for example, replace the data by the number of days since the first date. Does it improve accuracy?
* Use transformer to add polynomial features. Which effect does it have?

#### Training Decision Tree

* Train decision tree model on the original dataset. What is the accuracy?
* Visualize shallow decision tree and make conclusions about interpretability of the model.

