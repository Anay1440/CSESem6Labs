arr = list(map(int, input("Enter numbers ").split(' ')))
arr.sort()
n = int(input("Enter the number to search for "))
start, mid, end = 0, 0, len(arr) - 1
mid = (start + end) // 2
while (start <= end):
    if (arr[mid] > n):
        end = mid - 1
    elif (arr[mid] < n):
        start = mid + 1
    else:
        print("Element found")
        break
    mid = (start + end) // 2
else:
    print("Element not found")