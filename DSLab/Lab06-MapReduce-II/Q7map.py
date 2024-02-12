import random

with open('random_numbers.txt', 'w') as file:
    for i in range(500):
        n = random.randint(1, 10000)
        file.write(str(n) + "\n")

with open('random_numbers.txt', 'r') as file:
    for line in file:
        num = line.strip()
        if (int(num) % 2 == 0):
            print(f"Even\t{1}")
        else:
            print(f"Odd\t{1}")