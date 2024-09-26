import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns 

car_prices_df = pd.read_csv(r'C:\Users\abby1\Documents\DTA Project\car_prices.csv')

# Verifying the variable by showing the first few rows again
car_prices_df.head()
# Group the data by 'state' and calculate the average selling price
state_avg_price = car_prices_df.groupby('state')['sellingprice'].mean().sort_values(ascending=False).reset_index()

# Create the bar chart
sns.set_theme(style="whitegrid")

plt.figure(figsize=(10,6))
sns.barplot(x='state', y='sellingprice', data=state_avg_price, palette='Blues_d')

# Add titles and labels
plt.title('Average Car Selling Price by State', fontsize=14)
plt.xlabel('State', fontsize=12)
plt.ylabel('Average Selling Price (USD)', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()