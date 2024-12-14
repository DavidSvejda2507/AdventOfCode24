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
    
def neighbors(i:int, j:int):
    output = []
    if i>0:
        output.append((i-1, j))
    if j>0:
        output.append((i, j-1))
    if i<num_rows-1:
        output.append((i+1, j))
    if j<num_cols-1:
        output.append((i, j+1))
    return output

def measure(i: int, j:int):
    add_to_queue(i, j)
    area = 0
    perimeter = 0
    crop = field[i][j]
    
    while not queue.empty():
        row, col = queue.get()
        area += 1
        neighbor_list = neighbors(row, col)
        for a,b in neighbor_list:
            if field[a][b] == crop:
                if not checked[b + a * num_cols]:
                    add_to_queue(a, b)
            else:
                perimeter += 1
        perimeter += 4-len(neighbor_list)
        
    return area * perimeter

for i in range(num_rows):
    for j in range(num_cols):
        if not checked[j + i * num_cols]:
            total_cost += measure(i, j)
            
print(total_cost)