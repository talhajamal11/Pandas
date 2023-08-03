"""
1. Create a series with the temperature values for the last seven days. 
    Filter out the values below the mean.
2. Create a series with your favorite colors. Use a categorical type.
"""
import pandas as pd

temp = pd.Series(data=[30, 26, 32, 27, 36, 31, 28],
          index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
          dtype='int64',
          name="Temperature")

print(temp)
print(f'The Mean Temperature is {temp.mean()} \n')
low_temp = temp < temp.mean()
print(temp[low_temp])

colours = pd.Series(
    data=['Red', 'Blue', 'Green', 'Orange', 'Black', 'Brown'],
    dtype='category',
)
print("------------------")
print(colours)

print(colours.cat.ordered)
