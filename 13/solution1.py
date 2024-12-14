import re as RE

def parse(tup):
    return (int(tup[0]), int(tup[1]))

with open("input.txt") as f:
    machines = []
    first = RE.compile(r"Button A: X\+(\d+), Y\+(\d+)")
    second = RE.compile(r"Button B: X\+(\d+), Y\+(\d+)")
    third = RE.compile(r"Prize: X=(\d+), Y=(\d+)")
    while(True):
        line = f.readline()
        if (line == ""): break
        a = (first.match(line).groups())
        b = (second.match(f.readline()).groups())
        c = (third.match(f.readline()).groups())
        f.readline()
        
        machines.append((parse(a), parse(b), parse(c)))
    
def optimise(a, b, goal):
    for i in range(100):
        for j in range(100):
            if i*a[0] + j*b[0] == goal[0]:
                if i*a[1] + j*b[1] == goal[1]:
                    return 3*i + j
    return 0
                    
cost = 0    
for machine in machines:
    cost += optimise(*machine)
    
print(cost)