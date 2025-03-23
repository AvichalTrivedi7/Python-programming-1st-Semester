import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Writing to CSV
df.to_csv('sample.csv', index=False)
print("CSV file 'sample.csv' has been saved.")

# Reading from CSV
df_read = pd.read_csv('sample.csv')
print("\nData read from 'sample.csv':")
print(df_read)
