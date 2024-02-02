class Power:
    def pow(self, n, p):
        return n ** p
    
if __name__ == "__main__":
    n = int(input("Enter number "))
    p = int(input("Enter power "))
    obj = Power()
    print("Result:", obj.pow(n, p))