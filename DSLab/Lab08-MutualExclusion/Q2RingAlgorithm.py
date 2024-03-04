n = int(input("Enter total number of nodes "))
dead_nodes = list(map(int, input("Enter node indexes that are dead separated by space ").split(' ')))
start = int(input("Enter node that should start the election "))

curr = (start + 1) % n

list_of_nodes = [start]

while curr != start:
    while curr in dead_nodes:
        curr = (curr + 1) % n
    list_of_nodes.append(curr)
    print(f"At node {curr} the list of nodes is {list_of_nodes}")
    curr = (curr + 1) % n

print("Coordinator is:", max(list_of_nodes))