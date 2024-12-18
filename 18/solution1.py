with open("input.txt") as f:
    input_list = []
    while True:
        line = f.readline()
        if line == "": break
        
        input_list.append(list(map(int, line.split(","))))
        

map_ = [[-1]*71 for _ in range(71)]

for x, y in input_list[:1024]:
    map_[x][y] = "#"
    
def neighbors(i:int, j:int):
    output = []
    if i>0:
        output.append((i-1, j))
    if j>0:
        output.append((i, j-1))
    if i<70:
        output.append((i+1, j))
    if j<70:
        output.append((i, j+1))
    return output

def print_map(map_):
    for line in map_:
        print(*map(lambda x: x if x=="#" else ("." if x == -1 else "O"), line), sep = "")
    
i = 0
map_[0][0] = 0
updated = True
while updated:
    updated = False
    for x in range(71):
        for y in range(71):
            if map_[x][y] == i:
                for x_, y_ in neighbors(x, y):
                    if map_[x_][y_] == -1:
                        map_[x_][y_] = i+1
                        updated = True
    if map_[70][70] != -1:
        break
    i+=1

print(map_[70][70])