# with open("test.txt") as f:
with open("input.txt") as f:
    connections = []
        
    while True:
        line = f.readline()
        if line == "": break
        connections.append((line[0:2], line[3:5]))
        
for i, pair in enumerate(connections):
    if pair[1] < pair[0]:
        connections[i] = (pair[1], pair[0])
        
connections.sort()

current = ""
tripples = []
for i, pair in enumerate(connections):
    first, second = pair
    if first != current:
        current = first
    for pair_two in connections[i+1:]:
        if pair_two[0] != current:
            break
        if (second, pair_two[1]) in connections:
            tripples.append((first, second, pair_two[1]))
        
count = 0
for tripple in tripples:
    if any(map(lambda x: x[0] == "t", tripple)):
        count += 1
        
print(count)
        
