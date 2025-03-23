import pandas as pd
import numpy as np

data = {'Name': ['Alice', 'Bob', np.nan, 'David'],
        'Age': [25, np.nan, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', np.nan]}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nFilling missing values:")
df_filled = df.fillna("Unknown")
print(df_filled)

print("\nDropping rows with missing values:")
df_dropped = df.dropna()
print(df_dropped)
