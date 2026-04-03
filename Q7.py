import pandas as pd

df = pd.read_csv("customerData.csv")
age_df = df[["age"]].head(100)
print(age_df)