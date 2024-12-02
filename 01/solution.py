
with open("input.txt") as f:
    first  = []
    second = []
    while(True):
        line = f.readline()
        if (line == ""): break
        a,b = line.split()
        first.append(int(a))
        second.append(int(b))
        
first.sort()
second.sort()
sum = sum(map(lambda tup:abs(tup[0]-tup[1]),zip(first, second)))
print(sum)
