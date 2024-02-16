from matplotlib import pyplot as plt 

in_file = open("out.txt", 'r')
data = {}
for line in in_file:
    inp = line.split('\t')
    if (inp[1][-1] == '\n'):
        inp[1] = inp[1][:-1].strip()
    if (float(inp[1]) > 200000):
        data[inp[0]] = float(inp[1])
    else:
        try: 
            if (data["Other"]):
                data["Other"] = data["Other"] + float(inp[1])
        except(Exception):
            data["Other"] = float(inp[1])

fig = plt.figure(figsize=(10, 7))
plt.pie(data.values(), labels=data.keys())
# plt.bar(x=data.keys(), height=data.values())

plt.show()