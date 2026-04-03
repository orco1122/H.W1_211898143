import pandas as pd

# Q10.a
df = pd.read_csv("customerData.csv")
df.columns = df.columns.str.strip()
females_df = df[df["gender"] == "F"]
housing_counts_f = females_df["housing_type"].value_counts()
most_popular_f = housing_counts_f.idxmax()
print(most_popular_f)
# Q10.b
males_df = df[df["gender"] == "M"]
housing_counts_m = males_df["housing_type"].value_counts()
most_popular_m = housing_counts_m.idxmax()
print(most_popular_m)
