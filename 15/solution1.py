with open("input.txt") as f:
    map_ = []
    steps = []
    while(True):
        line = f.readline()
        if (line == "\n"): break
        
        map_.append(list(map(lambda x: line[x], range(len(line)-1))))
    
    while(True):
        line = f.readline()
        if (line == ""): break
        
        steps.extend(map(lambda x: line[x], range(len(line)-1)))
        
pos = (0,0)

for x, row in enumerate(map_):
    for y, space in enumerate(row):
        if space == "@":
            pos = (x,y)
            
def move(dx:int, dy:int, pos:tuple[int, int])->tuple[int, int]:
    x, y = pos
    while True:
        x += dx
        y += dy
        if map_[x][y] == "#":
            return pos
        elif map_[x][y] == "O":
            pass
        elif map_[x][y] == ".":
            x_, y_ = pos
            x_ += dx
            y_ += dy
            map_[x][y] = map_[x_][y_]
            map_[x_][y_] = "@"
            map_[pos[0]][pos[1]] = "."
            return (x_, y_)
        else:
            print("Hey, You")
          
for step in steps:
    if step == "^":
        pos = move(-1, 0, pos)
    elif step == ">":
        pos = move(0, 1, pos)
    elif step == "v":
        pos = move(1, 0, pos)
    elif step == "<":
        pos = move(0, -1, pos)
    else:
        print("Hey")
        
sum_ = 0
for x, row in enumerate(map_):
    for y, space in enumerate(row):
        if space == "O":
            sum_ += 100*x + y
            
print(sum_)