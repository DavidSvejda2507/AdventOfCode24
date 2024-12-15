import re as RE

def parse(tup):
    return (int(tup[0]), int(tup[1]), int(tup[2]), int(tup[3]))

with open("input.txt") as f:
    robots = []
    first = RE.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")
    while(True):
        line = f.readline()
        if (line == ""): break
        
        a = parse(first.match(line).groups())
        robots.append(parse(a))

rows = 103
cols = 101
image = [0]*rows*cols

def print_tree(positions:dict[tuple[int, int], int]):
    image = [0]*rows*cols

    for pos in positions:
        image[cols*pos[1]+pos[0]] = 1
    
    for y in range(rows):
        print(*map(lambda x: "X" if x==1 else " ", image[y*cols:(y+1)*cols]))
    


for i in range(101*103):
    positions = {}
    success = True
    for robot in robots:
        x = (robot[0] + i*robot[2])%cols
        y = (robot[1] + i*robot[3])%rows
        
        if positions.get((x,y), 0) != 0:
            success = False
            break
        else:
            positions[(x,y)] = 1
    
    if success:
        print_tree(positions)
        input(i)

