## Homework 1:

import pandas as pd
import numpy as np

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)

## Rename column names using function. "First Name" --> "first_name", "Age" --> "age
## Print the first 3 rows of the DataFrame
## Find the mean age of the individuals
## Select and print only the 'Name' and 'City' columns
## Add a new column 'Salary' with random salary values
## Display summary statistics of the DataFrame

def rename_cols(col):
    return col.strip().lower().replace(" ", "_")
df = df.rename(columns=rename_cols)

print(df.head(3))

df1=df['age'].mean()

df2=df[['first_name','age']]
print(df2)

df['Salary']=np.random.randint(5000, 10000, 4)

print(df.describe())

## Homework 2:
## Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.
## Calculate and display the maximum sales and expenses.
## Calculate and display the minimum sales and expenses.
## Calculate and display the average sales and expenses.

sales_and_expenses=pd.DataFrame({'Month':['Jan','Feb','Mar','Apr'],
                                 'Sales':[5000,6000,7500,8000],
                                 'Expenses':[3000,3500,4000,4500]}
                                )
print(sales_and_expenses)
sale_max=sales_and_expenses['Sales'].max()
expenses_max=sales_and_expenses['Expenses'].max()
print(f'Maximum sales:{sale_max}, Expenses maximum: {expenses_max}')

sale_min=sales_and_expenses['Sales'].min()
expenses_min=sales_and_expenses['Expenses'].min()
print(f'Minimum sales:{sale_min}, Expenses minimum: {expenses_min}')

sale_avg=sales_and_expenses['Sales'].mean()
expenses_avg=sales_and_expenses['Expenses'].mean()
print(f'Average sales:{sale_avg}, Average expenses: {expenses_avg}')

## Homework 3:
##Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.

expenses=pd.DataFrame({'Category':['Rent','Utilities','Groceries','Entertainment'],
                       'January':[1200,200,300,150],
                       'February':[1300,220,320,160],
                       'March':[1400,240,330,170],
                       'April':[1500,250,350,180]}
                      ).set_index('Category')
print(expenses)
category_max=expenses.max(axis=1)
print(category_max)
category_min=expenses.min(axis=1)
print(category_min)
category_mean=expenses.mean(axis=1)
print(category_mean)
