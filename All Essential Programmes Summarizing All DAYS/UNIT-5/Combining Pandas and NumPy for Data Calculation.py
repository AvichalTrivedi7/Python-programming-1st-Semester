import pandas as pd
import numpy as np

data = {'Product': ['A', 'B', 'C', 'D'],
        'Price': [100, 200, 150, 300],
        'Quantity': [2, 3, 5, 1]}

df = pd.DataFrame(data)

# Calculating total cost using NumPy
df['Total Cost'] = np.multiply(df['Price'], df['Quantity'])

print("Updated DataFrame with Total Cost:")
print(df)
