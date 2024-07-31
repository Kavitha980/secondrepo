import pandas as pd
import matplotlib.pyplot as plt
import csv



def extract_column_names(csv_file):
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        # print(type(csv_reader))

        # Assuming the first row contains column headers
        # retune the first line(row) and then(next) move to second row
        column_names = next(csv_reader)

        # now csv_reader have elements of file except first row(ie column name)
        # declared as set to make sure to add unique elements only
        unique_row_names = []  # Initialize an empty list to store unique row names in order
        row_names = set()
        for row in csv_reader:
            # Assuming row names are in the first column
            row_name = row[0]  # Assuming row names are in the first column

            if row_name not in unique_row_names:
                unique_row_names.append(row_name)  # Add row name to list
                # row_names.add(row_name)

    return column_names, unique_row_names


# Example usage:
#csv_file = 'Exams list-4.csv'
csv_file = 'data.csv'
column_names, row_names = extract_column_names(csv_file)
print("Column Names:", column_names)
print("Row Names:", row_names)

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Getting input from the user
x_value = input("Enter X Axis value: ")
y_value = input("Enter Y Axis value: ")


# Extract data for plotting
x_plot = df[x_value]
y_plot = df[y_value]


# Create different types of plots
plt.figure(figsize=(10, 6))

# Line plot for Revenue and Expenses over Years
plt.subplot(2, 2, 1)
plt.plot(x_plot, y_plot, marker='o', linestyle='-', color='b', label=str(x_value))
# plt.plot(x_plot, y_plot, marker='o', linestyle='-', color='r', label=str(y_value))
plt.xlabel(str(x_value))
plt.ylabel(str(y_value))
plt.title(str(x_value) + " with "+ str(y_value)  )
plt.legend()

# Bar plot for Profit over Years
plt.subplot(2, 2, 2)
plt.bar(x_plot, y_plot, color='g', alpha=0.9)
plt.xlabel(str(x_value))
plt.ylabel(str(y_value))
plt.title(str(x_value) + " with "+ str(y_value)  )
plt.legend()

# Horizontal bar plot for Profit Comparison
plt.subplot(2, 2, 3)
plt.barh(x_plot, y_plot, color='purple', alpha=0.6)
plt.xlabel(str(x_value))
plt.ylabel(str(y_value))
plt.title(str(x_value) + " with "+ str(y_value)  )
plt.legend()

# Histogram of Revenue distribution
plt.subplot(2, 2, 4)
plt.hist(x_plot, bins=5, edgecolor='black')
plt.xlabel(str(x_value))
plt.ylabel(str(y_value))
plt.title(str(x_value) + " with "+ str(y_value)  )
plt.legend()

# donut chat


# Save the plot to a file
plt.savefig('plot.png')

# Show the plot
plt.show()