with open("input.txt") as f:
    map_:list[list[str]] = []
    while(True):
        line = f.readline()
        if (line == ""): break
        map_.append(list(map(lambda x: line[x], range(len(line)-1))))
    
for index, line in enumerate(map_):
    if "^" in line:
        row = index
        break
    
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
    
col = map_[row].index("^")
steps = [(-1,0),(0,1),(1,0),(0,-1)]
direction = 0
map_[row][col] = "0"
while(inBounds(row, col, steps[direction])):
    new_row = row+steps[direction][0]
    new_col = col + steps[direction][1]
    if map_[new_row][new_col]=="#":
        direction = (direction+1)%4
    else:
        row = new_row
        col = new_col
        map_[row][col] = direction
    
print(sum(map(lambda x: sum(map(lambda y: 1 if y=="x" else 0, x)), map_)))
