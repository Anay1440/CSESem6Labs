import numpy as np

r = int(input("Enter number of rows "))
c = int(input("Enter number of columns "))
mat = np.zeros((r, c), int)
for i in range(r):
    for j in range(c):
        mat[i][j] = int(input(f"Enter a[{i}][{j}] "))
print("Given matrix:\n", mat)
mat = mat.T
print("Transposed matrix:\n", mat)