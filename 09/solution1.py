with open("input.txt") as f:
    while(True):
        line = f.readline()
        if (line == ""): break
        fs=(list(map(lambda x: int(line[x]), range(len(line)-1))))
        
n_files = (len(fs)+1)//2

front = 0
back = len(fs)-1

sum_ = 0
index = 0
while True:
    for i in range(fs[front]):
        sum_ += (front//2)*index
        index += 1
    
    if front == back:
        break
        
    front += 1
    
    for i in range(fs[front]):
        sum_ += (back//2)*index
        index += 1
        fs[back] -= 1
        if fs[back] == 0:
            back -= 2
            if back < front:
                break
    
    if back<front:
        break
    
    front += 1
    
print(sum_)