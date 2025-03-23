import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 28],
        'Salary': [50000, 60000, 55000, 70000, 62000]}

df = pd.DataFrame(data)

# Filtering employees with Age > 30 and Salary > 55000
filtered_df = df[(df['Age'] > 30) & (df['Salary'] > 55000)]

print("Filtered DataFrame:")
print(filtered_df)
