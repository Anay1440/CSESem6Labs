class StringIO:
    def __init__(self):
        self.str = ""

    def get_string(self):
        self.str = input("Enter string ")
    
    def print_string(self):
        print(self.str.upper())
    
if __name__ == "__main__":
    obj = StringIO()
    obj.get_string()
    print("Output:", end=" ")
    obj.print_string()    