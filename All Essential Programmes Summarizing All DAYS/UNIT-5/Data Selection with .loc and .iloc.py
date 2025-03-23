import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# Using .loc (label-based selection)
print("Using .loc to select first row:")
print(df.loc[0])

# Using .iloc (position-based selection)
print("\nUsing .iloc to select second row:")
print(df.iloc[1])
