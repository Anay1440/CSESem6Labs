in_file = open("Text.txt", 'r')
out_file = open("Out.txt", "w+")
for line in in_file:
    out_file.write(line[::-1])
print("Completed")