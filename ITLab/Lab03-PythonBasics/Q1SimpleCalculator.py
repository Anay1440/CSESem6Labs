n1 = float(input("Enter first number "))
n2 = float(input("Enter second number "))
op = input("Enter operator ")
out = 0
if op == '+':
    out = n1 + n2
elif op == '-':
    out = n1 - n2
elif op == '*':
    out = n1 * n2
elif op == '/':
    out = n1 / n2
print(f"Output: {n1} {op} {n2} = {out}")