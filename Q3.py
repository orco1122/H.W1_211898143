import pandas as pd
df=pd.read_csv('customerData.csv')
new_df = df.iloc[::10, ::2]
print(new_df.head())