import numpy as np

r = int(input("Enter number of rows "))
c = int(input("Enter number of columns "))
mat1 = np.zeros((r, c), int)
mat2 = np.zeros((r, c), int)
print("Enter values for first matrix")
for i in range(r):
    for j in range(c):
        mat1[i][j] = int(input(f"Enter a[{i}][{j}] "))
print("Enter values for second matrix")
for i in range(r):
    for j in range(c):
        mat2[i][j] = int(input(f"Enter a[{i}][{j}] "))
print("Mat1:\n",mat1,"\nMat2:\n", mat2)
mat1 = mat1 + mat2
print("Result:\n", mat1)