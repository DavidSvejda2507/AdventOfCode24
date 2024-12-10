

with open("input.txt") as f:
    map_:list[list[list[int, int]]] = []
    while(True):
        line = f.readline()
        if (line == ""): break
        map_.append(list(map(lambda x: [int(line[x]), 0], range(len(line)-1))))
        

def neighbors(i:int, j:int):
    output = []
    if i>0:
        output.append((i-1, j))
    if j>0:
        output.append((i, j-1))
    if i<len(map_)-1:
        output.append((i+1, j))
    if j<len(map_[0])-1:
        output.append((i, j+1))
    return output

for i in range(len(map_)):
    for j in range(len(map_[0])):
        if map_[i][j][0] == 9:
            map_[i][j][1] = 1

for h in range(8,-1, -1):            
    for i in range(len(map_)):
        for j in range(len(map_[0])):
            if map_[i][j][0] == h:
                for a,b in neighbors(i, j):
                    if map_[a][b][0] == h+1:
                        map_[i][j][1] += map_[a][b][1]
                        
            
print(sum(map(lambda x:sum(map(lambda y:y[1] if y[0] == 0 else 0, x)), map_)))