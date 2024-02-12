import fileinput
max_value = -1
old_key = None
for line in fileinput.input():
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    current_key, current_value = data
    if old_key and old_key != current_key:
        print(old_key,"\t", max_value)
        max_value = -1
    if float(current_value) > float(max_value):
        max_value = float(current_value)
        old_key = current_key
if old_key != None:
    print (old_key, "\t", max_value)