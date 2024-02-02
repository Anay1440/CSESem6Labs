class Subsets:
    subsets = []
    def get_subsets(self, arr):
        all_subsets = [[]]
        for i in arr:
            curr_subsets = []
            for subset in all_subsets:
                curr_subsets.append(subset + [i])
            all_subsets.extend(curr_subsets)
        return all_subsets

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers ").split(' ')))
    obj = Subsets()
    print("Subsets:", obj.get_subsets(arr))
                