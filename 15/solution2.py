def widen(line):
    output = []
    for elem in line:
        if elem == "#":
            output.extend(["#", "#"])
        elif elem == "O":
            output.extend(["[", "]"])
        elif elem == "@":
            output.extend(["@", "."])
        elif elem == ".":
            output.extend([".", "."])
        else:
            print("Hey")
    return output

# with open("test.txt") as f:
with open("input.txt") as f:
    map_ = []
    steps = []
    while(True):
        line = f.readline()
        if (line == "\n"): break
        
        map_.append(list(map(lambda x: line[x], range(len(line)-1))))
    
    wide_map = []
    for line in map_:
        wide_map.append(widen(line))
    map_ = wide_map
    
    while(True):
        line = f.readline()
        if (line == ""): break
        
        steps.extend(map(lambda x: line[x], range(len(line)-1)))
        
pos = (0,0)

for x, row in enumerate(map_):
    for y, space in enumerate(row):
        if space == "@":
            pos = (x,y)
            
def print_map(map_):
    for row in map_:
        print(*row, sep="")
            
def move_y(dy:int, pos:tuple[int, int])->tuple[int, int]:
    x, y = pos
    while True:
        y += dy
        if map_[x][y] == "#":
            return pos
        elif map_[x][y] == "[":
            pass
        elif map_[x][y] == "]":
            pass
        elif map_[x][y] == ".":
            x_, y_ = pos
            if dy == 1:
                map_[x][y_+1:y+1] = map_[x][y_:y]
                map_[x][y_] = "."
            elif dy == -1:
                map_[x][y:y_] = map_[x][y+1:y_+1]
                map_[x][y_] = "."
            else:
                raise ValueError()
            map_[x][y_] = "."
            return (x_, y_+dy)
        else:
            print("Hey, You")
            
def move_x(dx:int, pos:tuple[int, int]):
    x, y = pos
    y_list = [[y]]
    next_y_list = []
    while True:
        x += dx
        for y in y_list[-1]:
            if map_[x][y] == "#":
                return pos
            elif map_[x][y] == "[":
                if not (y) in next_y_list:
                    next_y_list.append(y)
                if not (y+1) in next_y_list:
                    next_y_list.append(y+1)
            elif map_[x][y] == "]":
                if not (y-1) in next_y_list:
                    next_y_list.append(y-1)
                if not (y) in next_y_list:
                    next_y_list.append(y)
            elif map_[x][y] == ".":
                pass
            else:
                print("Hey, You")
        if len(next_y_list) == 0:
            for ys in reversed(y_list):
                x -= dx
                for y in ys:
                    map_[x+dx][y] = map_[x][y]
                    map_[x][y] = "."
            return (x+dx, y)
        else:
            y_list.append(next_y_list)
            next_y_list = []
          
print_map(map_)
for step in steps:
    if step == "^":
        pos = move_x(-1, pos)
    elif step == ">":
        pos = move_y(1, pos)
    elif step == "v":
        pos = move_x(1, pos)
    elif step == "<":
        pos = move_y(-1, pos)
    else:
        print("Hey")
    # print(step)
    # print_map(map_)
    # input()
        
sum_ = 0
for x, row in enumerate(map_):
    for y, space in enumerate(row):
        if space == "[":
            sum_ += 100*x + y
            
print(sum_)
