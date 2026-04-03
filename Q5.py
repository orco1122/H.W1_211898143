import pandas as pd

df = pd.read_csv("customerData.csv")
news_df_age = df[(df["age"] >= 38) & (df["age"] <= 50)]
print(news_df_age)