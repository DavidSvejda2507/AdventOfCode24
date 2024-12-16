import queue as Q
import itertools

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
            map_[x][y] = [[-1], [-1], [-1], [-1]]
        elif spot == "#":
            pass
        elif spot == "S":
            map_[x][y] = [[-1], [0, ""], [-1], [-1]]
            start = (x, y)
        elif spot == "E":
            map_[x][y] = [[-1], [-1], [-1], [-1]]
            end = (x, y)
        else:
            print("Hey")
            
queue = Q.PriorityQueue()
queue.put((0, len(map_)-2, 1, 1))

def update(cost, x, y, dir, origin):
    current = map_[x][y][dir]
    if current[0] == -1 or current[0] > cost:
        map_[x][y][dir] = [cost, origin]
        queue.put((cost, x, y, dir))
    elif current[0] == cost:
        map_[x][y][dir].append(origin)
        
    
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
    if map_[x][y][dir][0] < cost:
        pass
    else:
        update(cost+1000, x, y, (dir-1)%4, "+")
        update(cost+1000, x, y, (dir+1)%4, "-")
        dx, dy = get_offset(dir)
        if map_[x+dx][y+dy] != "#":
            update(cost+1, x+dx, y+dy, dir, (dir+2)%4)
            
     
counter = itertools.count()
visited = []
for _ in range(len(map_)):
    visited.append([0]*len(map_[0]))

min_cost = min(*map_[end[0]][end[1]])[0]
for dir, cost in enumerate(map_[end[0]][end[1]]):
    if cost[0] == min_cost:
        for origin in cost[1:]:
            queue.put((cost[0], end[0], end[1], dir, counter.__next__(), origin))
        map_[end[0]][end[1]] = [cost[0]]
visited[end[0]][end[1]] = 1

def walk_back(x, y, dir, counter):
    cost = map_[x][y][dir]
    for origin in cost[1:]:
        queue.put((cost[0], x, y, dir, counter.__next__(), origin))
    map_[x][y][dir] = [cost[0]]
    visited[x][y] = 1
        

while not queue.empty():
    _, x, y, dir, _, origin = queue.get()
    if origin == "-":
        walk_back(x, y, (dir-1)%4, counter)
    elif origin == "+":
        walk_back(x, y, (dir+1)%4, counter)
    elif type(origin) == int:
        dx, dy = get_offset(dir)
        walk_back(x-dx, y-dy, dir, counter)
        
print(sum(map(sum, visited)))
    
