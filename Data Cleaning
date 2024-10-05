import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Sales_sample.csv')

missing_values = df.isnull().sum()
print("Missing Values per Column:\n", missing_values)

df.dropna(subset=['OrderDate', 'Region', 'Rep', 'Item'], inplace=True)

df['Units'].fillna(df['Units'].mean(), inplace=True)
df['Unit Cost'].fillna(df['Unit Cost'].mean(), inplace=True)

units_per_item = df.groupby('Item')['Units'].sum()

total_units = units_per_item.sum()

units_per_item.plot(kind='bar', color='blue')

plt.xlabel('Items')
plt.ylabel('Total Units Sold')

plt.title('Total Units Sold per Item')

plt.show()
