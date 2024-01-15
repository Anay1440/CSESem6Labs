n = int(input("Enter a number "))
fact = 1
while n > 0:
    fact = fact * n
    n -= 1
else:
    print("Factorial: ", fact)