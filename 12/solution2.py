import queue as Q

with open("input.txt") as f:
    field = []
    while(True):
        line = f.readline()
        if (line == ""): break
        field.append(list(map(lambda x: line[x], range(len(line)-1))))

num_rows = len(field)
num_cols = len(field[0])
checked = [False] * num_rows * num_cols
queue = Q.Queue()
total_cost = 0

def add_to_queue(i: int, j: int):
    queue.put((i,j))
    checked[j + i * num_cols] = True
    
def neighbors(i:int, j:int)->tuple[list[tuple[int, int, tuple[int, tuple[int, int, int]]]],tuple[list[tuple[int, int, int]], list[tuple[int, int, int]]]]:
    neighbor_list = []
    edges = ([],[])
    if i>0:
        neighbor_list.append((i-1, j, (0,(i, j, -1))))
    else:
        edges[0].append((i, j, -1))
    if j>0:
        neighbor_list.append((i, j-1, (1,(i, j, -1))))
    else:
        edges[1].append((i, j, -1))
    if i<num_rows-1:
        neighbor_list.append((i+1, j, (0, (i+1, j, 1))))
    else:
        edges[0].append((i+1, j, 1))
    if j<num_cols-1:
        neighbor_list.append((i, j+1, (1, (i, j+1, 1))))
    else:
        edges[1].append((i, j+1, 1))
    return (neighbor_list, edges)

def measure(i: int, j:int):
    add_to_queue(i, j)
    area = 0
    crop = field[i][j]
    col_fences = []
    row_fences = []
    fences = (col_fences, row_fences)
    
    while not queue.empty():
        row, col = queue.get()
        area += 1
        neighbor_list, (col_fs, row_fs) = neighbors(row, col)
        col_fences.extend(col_fs)
        row_fences.extend(row_fs)
        for a,b,dir in neighbor_list:
            if field[a][b] == crop:
                if not checked[b + a * num_cols]:
                    add_to_queue(a, b)
            else:
                fences[dir[0]].append(dir[1])
    edges = 2            
    col_fences.sort(key = lambda x: (x[0], x[2], x[1]))
    current = col_fences[0]
    for next in col_fences[1:]:
        if next[0] == current[0] and next[2] == current[2] and next[1] == current[1] + 1:
            pass
        else: 
            edges += 1
        current = next
    row_fences.sort(key = lambda x: (x[1], x[2], x[0]))
    current = row_fences[0]
    for next in row_fences[1:]:
        if next[1] == current[1] and next[2] == current[2] and next[0] == current[0] + 1:
            pass
        else: 
            edges += 1
        current = next
    
        
    return area * edges

for i in range(num_rows):
    for j in range(num_cols):
        if not checked[j + i * num_cols]:
            total_cost += measure(i, j)
            
print(total_cost)
