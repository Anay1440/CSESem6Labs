tup = (12, 7, 38, 56, 78)
arr = []
for i in tup:
    if (i % 2 == 0):
        arr.append(i)
tup2 = tuple(arr)
print(tup2)