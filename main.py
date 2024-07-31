import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('data.csv')

# Extract data for plotting
years = df['Year']
revenue = df['Revenue']
expenses = df['Expenses']
profit = df['Profit']

# Create different types of plots
plt.figure(figsize=(10, 6))

# Line plot for Revenue and Expenses over Years
plt.subplot(2, 2, 1)
plt.plot(years, revenue, marker='o', linestyle='-', color='b', label='Revenue')
plt.plot(years, expenses, marker='o', linestyle='-', color='r', label='Expenses')
plt.xlabel('Year')
plt.ylabel('Amount ($)')
plt.title('Revenue and Expenses over Years')
plt.legend()

# Bar plot for Profit over Years
plt.subplot(2, 2, 2)
plt.bar(years, profit, color='g', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Profit ($)')
plt.title('Profit over Years')

# Horizontal bar plot for Profit Comparison
plt.subplot(2, 2, 3)
plt.barh(years, profit, color='purple', alpha=0.6)
plt.xlabel('Profit ($)')
plt.ylabel('Year')
plt.title('Profit Comparison')

# Histogram of Revenue distribution
plt.subplot(2, 2, 4)
plt.hist(revenue, bins=5, edgecolor='black')
plt.xlabel('Revenue ($)')
plt.ylabel('Frequency')
plt.title('Revenue Distribution')

# Adjust layout to prevent overlap
plt.tight_layout()

# Save the plot to a file
plt.savefig('plot.png')

# Show the plot
plt.show()
