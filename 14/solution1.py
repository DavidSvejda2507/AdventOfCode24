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

quads = [[0,0],[0,0]]

for robot in robots:
    x = (robot[0] + 100*robot[2])%cols
    y = (robot[1] + 100*robot[3])%rows
    
    if x == 50: continue
    if y == 51: continue
    
    if x<50:
        if y<51:
            quads[0][0] += 1
        else:
            quads[0][1] += 1
    else:
        if y<51:
            quads[1][0] += 1
        else:
            quads[1][1] += 1
            
print(quads[0][0]*quads[0][1]*quads[1][0]*quads[1][1])