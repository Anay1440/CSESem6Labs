arr = list(map(int, input("Enter numbers ").split(' ')))
posCount, negCount = 0, 0
for i in arr:
    if (i > 0):
        posCount += 1
    elif (i < 0):
        negCount += 1
print("Pos count: ", posCount, " Neg count: ", negCount)