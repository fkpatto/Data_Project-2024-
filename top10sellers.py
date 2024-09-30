import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the data
clean_df = pd.read_csv(r"C:\Users\jnrgs\OneDrive\Desktop\dta\cleaned_car_prices.csv")

# Group by seller and sum the sellingprice
top_sellers = clean_df.groupby('seller')['sellingprice'].sum().sort_values(ascending=False)

# Select the top 10 sellers
top_10_sellers = top_sellers.head(10)

# Plot the data for top 10 sellers
plt.figure(figsize=(10, 6))
sns.barplot(x=top_10_sellers.index, y=top_10_sellers.values, palette="Blues_d")
plt.title('Top 10 Sellers by Total Sales')
plt.xlabel('Seller')
plt.ylabel('Total Sales ($)')

# Apply the log scale to the y-axis
plt.yscale('log')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
