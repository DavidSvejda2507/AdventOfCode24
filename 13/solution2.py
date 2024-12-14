import re as RE

def parse(tup):
    return (int(tup[0]), int(tup[1]))

def parse_c(tup):
    return (int(tup[0]) + 10000000000000, int(tup[1]) + 10000000000000)

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
        
        machines.append((parse(a), parse(b), parse_c(c)))
    
def optimise(a, b, goal):
    a1, a2 = a
    b1, b2 = b
    g1, g2 = goal
    cost = 0
    
    in1 = (a1*g1 + a2*g2)/(a1**2 + a2**2)
    proj11, proj12 = a1*in1, a2*in1
    dif11, dif12 = g1 - proj11, g2 - proj12   
    in2 = (dif11*b1 + dif12*b2)/(dif11**2 + dif12**2)
    scale_b = round(1/in2)
    proj21, proj22 = b1/in2, b2/in2
    scale_a = round(((g1-proj21)/a1 + (g2-proj22)/a2)/2)
    if g1 == (scale_b * b1 + scale_a * a1) and g2 == (scale_b * b2 + scale_a * a2):
        return 3*scale_a + scale_b
    else:
        return 0
                    
cost = 0    
for machine in machines:
    cost += optimise(*machine)
    
print(cost)