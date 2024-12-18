with open("input.txt") as f:
    input_list = []
    while True:
        line = f.readline()
        if line == "": break
        
        input_list.append(list(map(int, line.split(","))))
    
def neighbors(i:int, j:int):
    output = []
    if i>0:
        output.append((i-1, j))
    if j>0:
        output.append((i, j-1))
    if i<70:
        output.append((i+1, j))
    if j<70:
        output.append((i, j+1))
    return output
        
def test(cutoff: int):
    # print(cutoff)
    map_ = [[-1]*71 for _ in range(71)]

    for x, y in input_list[:cutoff]:
        map_[x][y] = "#"
        
    i = 0
    map_[0][0] = 0
    updated = True
    while updated:
        updated = False
        for x in range(71):
            for y in range(71):
                if map_[x][y] == i:
                    for x_, y_ in neighbors(x, y):
                        if map_[x_][y_] == -1:
                            map_[x_][y_] = i+1
                            updated = True
        if map_[70][70] != -1:
            return True
        i+=1
    return False

lower = 1024
upper = 2048
while test(upper):
    upper *= 2

while True:
    if upper - lower == 1:
        break
    mid = (upper + lower)//2
    if test(mid):
        lower = mid
    else:
        upper = mid

print(input_list[lower])