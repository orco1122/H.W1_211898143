import pandas as pd

df = pd.read_csv("customerData.csv")
filtered_df = df[
    (df["marital_stat"].isin(["Married", "Divorced/Separated"])) & (df["age"] < 18)
]
print(filtered_df)