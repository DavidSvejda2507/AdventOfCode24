import itertools

with open("input.txt") as f:
    map_:list[list[str]] = []
    while(True):
        line = f.readline()
        if (line == ""): break
        map_.append(list(map(lambda x: line[x], range(len(line)-1))))
        
anti_nodes = [0]*len(map_)*len(map_[0])
frequencies = {}
for y, line in enumerate(map_):
    for x, freq in enumerate(line):
        if freq != ".":
            temp:list[tuple[int, int]] = frequencies.get(freq, [])
            temp.append((y, x))
            frequencies[freq] = temp
   
max_y = len(map_)
max_x = len(map_[0])
      
def add_anti_node(y:int, x:int):
    if y < 0:return
    if x < 0:return
    if y >= max_y:return
    if x >= max_x:return
    anti_nodes[max_x*y+x] = 1
       
def add_anti_nodes(first:tuple[int, int], second:tuple[int, int]):
    delta_y = first[0] - second[0]
    delta_x = first[1] - second[1]
    add_anti_node(first[0]+delta_y,  first[1]+delta_x)
    add_anti_node(second[0]-delta_y, second[1]-delta_x)
            
for key in frequencies:
    values = frequencies[key]
    for first, second in itertools.combinations(values, 2):
        add_anti_nodes(first, second)
        
print(sum(anti_nodes))