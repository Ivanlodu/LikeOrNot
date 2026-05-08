import pandas as pd

df = pd.read_csv('data/raw/dataset.csv')

print(df.head())          # first 5 rows
print(df.columns.tolist()) # all column names
print(df.shape)            # rows x columns
print(df.dtypes)           # data types
print(df.info())           # summary information
print(df.isnull().sum())   # missing values