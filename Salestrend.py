import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import os

print (os.getcwd())

# Sample data: Ensure your 'Date' column is in datetime format
# Replace with your actual data
data = {
    'Date': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01'],
    'Sales': [1000, 1500, 2000, 2500, 3000]
}
df = pd.read_csv(r'C:\Users\abby1\Documents\DTA Project\car_prices.csv')
df.head(), df.columns

# Convert 'saledate' to datetime format
df['saledate'] = pd.to_datetime(df['saledate'],errors='coerce')
print(df['saledate'].isna().sum()) 
df = df.dropna(subset=['saledate'])

# Plot using Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(df['saledate'], df['sellingprice'], marker='o', linestyle='-', color='b')
plt.title('Sales Trend Over Time')
plt.xlabel('saledate')
plt.ylabel('sellingprice')
plt.grid(True)
plt.legend()
plt.show()

# Alternatively, plot using Seaborn for a more stylized chart
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Sales', data=df, marker='o', color='g')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()