import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nAccessing first row:")
print(df.iloc[0])

print("\nAccessing 'Age' column:")
print(df['Age'])
