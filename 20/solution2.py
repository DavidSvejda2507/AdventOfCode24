import re as RE

# with open("test.txt") as f:
with open("input.txt") as f:
    map_ = []
        
    while True:
        line = f.readline()
        if line == "": break
        map_.append(list(map(lambda x: line[x], range(len(line)-1))))
        

for i in range(len(map_)):
    for j in range(len(map_[0])):
        if map_[i][j] == ".":
            map_[i][j] = -1
        if map_[i][j] == "S":
            map_[i][j] = 0
            start = (i,j)
            current = (i,j)
        if map_[i][j] == "E":
            map_[i][j] = -1
            end = (i,j)

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

def in_bounds(i:int, j:int):
    if i<0: return False
    if j<0: return False
    if i>len(map_)-1: return False
    if j>len(map_[0])-1: return False
    return True

distance = 1
while True:
    for x, y in neighbors(*current):
        if map_[x][y] == -1:
            map_[x][y] = distance
            distance += 1
            current = (x,y)
            
    if current == end:
        break

current = start
distance = 1
counts = {}
count = 0

        
while True:
    for dx in range(-20, 21):
        for dy in range(-20+abs(dx), 21-abs(dx)):
            x = current[0] + dx
            y = current[1] + dy
            if in_bounds(x, y):
                if map_[x][y] == "#":
                    continue
                cheat_distance = abs(dx) + abs(dy)
                if map_[x][y] >= map_[current[0]][current[1]] + cheat_distance + 100:
                    count += 1
    
    for x, y in neighbors(*current):
        if map_[x][y] == distance:
            current = (x,y)
            
    distance += 1
            
    if current == end:
        break

print(count)
