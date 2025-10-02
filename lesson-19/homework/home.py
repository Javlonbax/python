import pandas as pd

sales_df = pd.read_csv(r'D:/task/sales_data.csv')
sold_sum_df=sales_df.groupby('Category')['Quantity'].sum()
sold_mean_df=sales_df.groupby('Category')['Quantity'].mean()
sold_max_df=sales_df.groupby('Category')['Quantity'].max()
print(sold_mean_df)
