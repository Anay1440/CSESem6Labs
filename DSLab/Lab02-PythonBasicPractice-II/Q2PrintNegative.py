arr = list(map(int, input("Enter numbers ").split(' ')))
index = 0
while (index < len(arr)):
    if (arr[index] < 0):
        print(arr[index])
    index += 1