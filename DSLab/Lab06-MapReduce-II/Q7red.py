import sys

file = sys.stdin

dict = {}

for line in file:
    data = line.split('\t')
    if data[0] in dict.keys():
        dict[data[0]] += 1
    else:
        dict[data[0]] = 0

for key in dict.keys():
    print(f"{key}\t{dict[key]}")