# Write a python program to import and export data using Pandas and 
# show the details of the dataset like number of rows, columns, first five 
# rows, size, number of missing values, sum, average, min and max 
# values from the numerical columns.

import pandas as pd

# Import data from a CSV file
data = pd.read_csv('student-scores.csv')

# Display dataset details
print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])
print("\nFirst five rows:\n", data.head())
print("\nSize of the dataset:", data.size)

# Cheking if there is any missing values in Data set
print("\nNumber of missing values:\n", data.isnull().sum())

# Display summary statistics for numerical columns
# summision of all numerical values present in Dataset
print("\nSum of numerical columns:\n", data.sum(numeric_only=True))
print("\nAverage of numerical columns:\n", data.mean(numeric_only=True))
print("\nMinimum values of numerical columns:\n", data.min(numeric_only=True))
print("\nMaximum values of numerical columns:\n", data.max(numeric_only=True))

# Export data to a new CSV file
data.to_csv('output.csv', index=False)
