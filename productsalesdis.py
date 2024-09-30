import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the data
clean_df = pd.read_csv(r"C:\Users\jnrgs\OneDrive\Desktop\dta\cleaned_car_prices.csv")

# Group by 'make' and count the number of vehicles sold
product_sales = clean_df['make'].value_counts()

# Normalize the 'make' column to lowercase
clean_df['make'] = clean_df['make'].str.lower()

# Plot the product sales distribution
plt.figure(figsize=(12, 6))
sns.barplot(x=product_sales.index, y=product_sales.values, palette="coolwarm")
plt.title('Product Sales Distribution by Vehicle Company')
plt.xlabel('Vehicle Make')
plt.ylabel('Number of Vehicles Company')

# Apply the log scale to the y-axis
plt.yscale('log')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
