with open("input.txt") as f:
    lines = []
    while(True):
        line = f.readline()
        if (line == ""): break
        lines.append(list(map(lambda x: int(x), line.split())))
        
def safe(input):
    diffs = list(map(lambda tup:tup[0]-tup[1], zip(input[:-1], input[1:])))
    if any(x>0 for x in diffs) and any(x<0 for x in diffs): return False
    if any(x<-3 for x in diffs): return False
    if any(x==0 for x in diffs): return False
    if any(x>3 for x in diffs): return False
    return True

print(sum(map(lambda x: 1 if safe(x) else 0, lines)))