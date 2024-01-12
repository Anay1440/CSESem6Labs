n1, n2, n3 = map(int, input("Enter three numbers ").split(' '))
if (n1 >= n2 and n1 >= n3):
    print("Largest = ", n1)
elif (n2 >= n1 and n2 >= n3):
    print("Largest = ", n2)
else:
    print("Largest = ", n3)