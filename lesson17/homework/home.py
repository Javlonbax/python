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
