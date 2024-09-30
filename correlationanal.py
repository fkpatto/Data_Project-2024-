import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
clean_df = pd.read_csv(r"C:\Users\jnrgs\OneDrive\Desktop\dta\cleaned_car_prices.csv")

# Select numerical columns for correlation analysis
numerical_cols = ['odometer', 'condition', 'sellingprice', 'mmr']

# Compute the correlation matrix
correlation_matrix = clean_df[numerical_cols].corr()

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Analysis of Vehicle Features')
plt.show()
