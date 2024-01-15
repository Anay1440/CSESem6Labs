import pandas as pd
import numpy as np

arr = np.array([np.arange(0, 4), np.arange(5, 9), np.arange(10, 14)])

print(arr)
print("Sum of columns: ", arr.sum(axis = 1))
print("Sum of rows: ", arr.sum(axis = 0))