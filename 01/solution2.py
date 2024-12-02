
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
mapping = {}
for id in second:
    mapping[id] = mapping.get(id, 0)+1
print(mapping)
# sum = sum(map(lambda id:mapping.get(id,0), first))
sum = 0
for id in first:
    print(mapping.get(id, 0))
    sum += id*mapping.get(id, 0)
print(sum)
