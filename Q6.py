# Q6.a
import pandas as pd

df = pd.read_csv("customerData.csv")
numeric_seniors_df = df[df["age"] > 50].select_dtypes(include=["number"])
print(numeric_seniors_df.head())

# Q6.b
rows_filter = df.iloc[:, 9] > 50
target_columns = [0, 3, 8, 9]
new_df = df[rows_filter].iloc[:, target_columns]
print(new_df.head())