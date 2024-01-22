import numpy as np

print("Enter values for first matrix")
r1 = int(input("Enter number of rows "))
c1 = int(input("Enter number of columns "))
mat1 = np.zeros((r1, c1), int)
for i in range(r1):
    for j in range(c1):
        mat1[i][j] = int(input(f"Enter a[{i}][{j}] "))
print("Enter values for second matrix")
r2 = int(input("Enter number of rows "))
c2 = int(input("Enter number of columns "))
mat2 = np.zeros((r2, c2), int)
for i in range(r2):
    for j in range(c2):
        mat2[i][j] = int(input(f"Enter a[{i}][{j}] "))
print("Mat1:\n",mat1,"\nMat2:\n", mat2)
print("Elementwise product:\n", mat1 * mat2)