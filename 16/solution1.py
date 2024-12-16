import queue as Q

with open("input.txt") as f:
    map_ = []
    while(True):
        line = f.readline()
        if (line == ""): break
        
        map_.append(list(map(lambda x: line[x], range(len(line)-1))))

"""^ > v <"""

end = (0,0)
start = (0,0)

for x, row in enumerate(map_):
    for y, spot in enumerate(row):
        if spot == ".":
            map_[x][y] = [-1, -1, -1, -1]
        elif spot == "#":
            pass
        elif spot == "S":
            map_[x][y] = [-1, 0, -1, -1]
            start = (x, y)
        elif spot == "E":
            map_[x][y] = [-1, -1, -1, -1]
            end = (x, y)
        else:
            print("Hey")
            
queue = Q.PriorityQueue()
queue.put((0, len(map_)-2, 1, 1))

def update(cost, x, y, dir):
    current = map_[x][y][dir]
    if current == -1 or current > cost:
        map_[x][y][dir] = cost
    queue.put((cost, x, y, dir))
    
def get_offset(dir):
    if dir == 0:
        return (-1, 0)
    if dir == 1:
        return (0, 1)
    if dir == 2:
        return (1, 0)
    if dir == 3:
        return (0, -1)

while not queue.empty():
    cost, x, y, dir = queue.get()
    if map_[x][y][dir] < cost:
        pass
    else:
        update(cost+1000, x, y, (dir-1)%4)
        update(cost+1000, x, y, (dir+1)%4)
        dx, dy = get_offset(dir)
        if map_[x+dx][y+dy] != "#":
            update(cost+1, x+dx, y+dy, dir)
            
print(min(map_[end[0]][end[1]]))
    
