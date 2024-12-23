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

def find_tripples(connections:list):
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
    return tripples

def find_n_tuples(n_1_tuples:list, connections:list):
    n_tuples = []
    for i, set_ in enumerate(n_1_tuples):
        *first, second = set_
        first = tuple(first)
        for set_2 in n_1_tuples[i+1:]:
            if set_2[:-1] != first:
                break
            if (second, set_2[-1]) in connections:
                n_tuples.append((*first, second, set_2[-1]))
    return n_tuples

n_tuples = connections
while len(n_tuples) > 1:
    n_tuples = find_n_tuples(n_tuples, connections)
    print(len(n_tuples))
    
print(*n_tuples[0], sep = ",")
print(*sorted(n_tuples[0]), sep = ",")