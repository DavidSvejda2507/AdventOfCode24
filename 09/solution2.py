import itertools

with open("input.txt") as f:
# with open("test.txt") as f:
    while(True):
        line = f.readline()
        if (line == ""): break
        fs=(list(map(lambda x: int(line[x]), range(len(line)-1))))
# print(fs)
        
n_files = (len(fs)+1)//2
for i in range(n_files-1):
    fs[2*i+1] = [fs[2*i+1],[]]
for i in range(n_files):
    fs[2*i] = (fs[2*i],i)
# print(fs)
    
back = len(fs)-1

def print_fs(filesystem):
    for front in filesystem:
        if type(front)== tuple:
            for i in range(front[0]):
                print(front[1], end="")
        elif type(front) == list:
            for i in front[1]:
                print(i, end="")
            for i in range(front[0]):
                print(".", end="")
    print()

for back in range(len(fs)-1, 0, -2):
    size = fs[back][0]
    for i in range(back//2):
        j = 2*i + 1
        if fs[j][0] >= size:
            fs[j][0] -= size
            fs[j][1].extend(itertools.repeat(back//2, size))
            fs[back] = [size, []]
            # print_fs(fs)
            break
    
front = 0

sum_ = 0
index = 0
pos = 0

for front in fs:
    if type(front)== tuple:
        for i in range(front[0]):
            sum_ += (front[1])*index
            index += 1
    elif type(front) == list:
        for i in front[1]:
            sum_ += i*index
            index += 1
        index += front[0]
    else:
        print("Hey")
    
print(sum_)