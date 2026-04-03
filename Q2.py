#Q2a
import pandas as pd
df=pd.read_csv('customerData.csv')
print(df.describe())#for numeric data
print(df.describe(include=['object']))#for categorial data
#Q2b
print(df.dtypes)#showing the data types
#Q2c
#No Causality,High Cardinality,Overfitting

