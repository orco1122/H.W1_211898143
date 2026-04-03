# Q9.a
import pandas as pd

df = pd.read_csv("customerData.csv")
filtered_group = df[(df["income"] > 16000) & (df["state_of_res"] == "Washington")]
average_age = filtered_group["age"].mean()
print(average_age)
# Q9.b
max_age = filtered_group["age"].max()
print(max_age)
# Q9.c
min_income = filtered_group["income"].min()
print(min_income)
# Q9.d
count_costumers = len(filtered_group)
print(count_costumers)