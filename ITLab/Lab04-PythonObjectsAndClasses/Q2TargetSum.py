class Target_Sum:
    def get_pair(self, arr : list, target : int):
        for i in range(len(arr)):
            diff = target - arr[i]
            if (diff <= 0):
                continue
            ind = arr.index(diff)
            if (ind >= 0):
                return (i, ind)
        return (-1, -1)
    
if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers ").split(' ')))
    target = int(input("Enter target sum "))
    obj = Target_Sum()
    indices = obj.get_pair(arr, target)
    if (indices[0] == -1):
        print("No combination found")
    else:
        print("Indices:", indices)