arr = list(map(int, input("Enter numbers ").split(' ')))
n, removed, index = len(arr), 0, 0
while (index < n - removed):
    if (arr[index] % 2 == 0):
        arr.remove(arr[index])
        removed += 1
        index -= 1
    index += 1
print(arr)