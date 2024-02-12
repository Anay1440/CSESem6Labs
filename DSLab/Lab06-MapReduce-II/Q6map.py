import fileinput
ind = 0
for line in fileinput.input():
    data = line.strip().split(",")
    if ind == 0:
        ind += 1
        continue
    if len(data)==8:
        _, _, _, country, _, confirmed_count, _, _ = data
        print("{0}\t{1}".format(country, confirmed_count))