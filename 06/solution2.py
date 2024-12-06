import copy

# with open("test.txt") as f:
with open("input.txt") as f:
    map_:list[list[str]] = []
    while(True):
        line = f.readline()
        if (line == ""): break
        map_.append(list(map(lambda x: line[x], range(len(line)-1))))

    
def inBounds(row, col, step):
    if row==0:
        return False
    if row == len(map_)-1:
        return False
    if col==0:
        return False
    if col== len(map_[0])-1:
        return False
    return True

def tryObstacle(row_, col_, dir_, map):
    if not inBounds(row_, col_, steps[dir_]): return 0
    new_row_ = row_ + steps[dir_][0]
    new_col_ = col_ + steps[dir_][1]
    if map[new_row_][new_col_]!=".":
        return 0
    map[new_row_][new_col_] = "O"
    dir_ = (dir_+1)%4
    
    while(inBounds(row_, col_, steps[dir_])):
        new_row_ = row_ + steps[dir_][0]
        new_col_ = col_ + steps[dir_][1]
        if map[new_row_][new_col_]=="#" or map[new_row_][new_col_]=="O":
            dir_ = (dir_+1)%4
        else:
            row_ = new_row_
            col_ = new_col_
            if map[row_][col_] == dir_: 
                return 1
            map[row_][col_] = dir_
    return 0
    
steps = [(-1,0),(0,1),(1,0),(0,-1)]
    
for index, line in enumerate(map_):
    if "^" in line:
        row = index
        break
col = map_[row].index("^")
direction = 0
map_[row][col] = "0"
loops = tryObstacle(row, col, direction, copy.deepcopy(map_))
while(inBounds(row, col, steps[direction])):
    new_row = row+steps[direction][0]
    new_col = col + steps[direction][1]
    if map_[new_row][new_col]=="#":
        direction = (direction+1)%4
        loops += tryObstacle(row, col, direction, copy.deepcopy(map_))
    else:
        row = new_row
        col = new_col
        map_[row][col] = direction
        loops += tryObstacle(row, col, direction, copy.deepcopy(map_))
    
    
    
    
print(loops)
