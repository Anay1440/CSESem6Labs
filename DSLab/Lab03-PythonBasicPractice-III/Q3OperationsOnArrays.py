import numpy as np

# Part a
l = [10, 9, -2, 3]
arr = np.array(l, dtype=float)
print(arr)

# Part b
tup = (10, 9, -2, 3.2)
arr = np.array(tup)
print(arr)

# Part c
arr = np.zeros((3, 4))
print(arr)

# Part d
arr = np.arange(0, 21, step=5)
print(arr)

# Part e
arr = np.array([np.arange(0, 4), np.arange(5, 9), np.arange(10, 14)])
arr = arr.reshape((2, 2, 3))
print(arr)

# Part f
arr = np.array([np.arange(0, 4), np.arange(5, 9), np.arange(10, 14)])
print(arr)
print("Maximum element: ", arr.max(), "\nMinimum element: ", arr.min())
print("Sum of columns: ", arr.sum(axis = 0))
print("Columnwise max: ", arr.max(axis = 0))
print("Columnwise min: ", arr.min(axis = 0))
print("Row wise max: ", arr.max(axis = 1))
print("Row wise min: ", arr.min(axis = 1))