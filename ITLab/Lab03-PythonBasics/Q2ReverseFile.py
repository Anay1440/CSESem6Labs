in_file = open("Text.txt", 'r')
out_file = open("Out.txt", "w+")
out_file.write(in_file.read()[::-1])
print("Completed")