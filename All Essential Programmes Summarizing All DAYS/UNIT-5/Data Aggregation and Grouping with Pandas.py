import pandas as pd

data = {'Department': ['HR', 'IT', 'HR', 'IT', 'Finance'],
        'Salary': [50000, 60000, 55000, 70000, 65000]}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

grouped = df.groupby('Department')['Salary'].mean()
print("\nAverage salary by department:")
print(grouped)
