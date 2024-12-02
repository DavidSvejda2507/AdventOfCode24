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

def safer(input_:list[int]):
    return any(map(lambda x:safe(x), (list(zip(*filter(lambda x: x[1] != i, zip(input_, range(len(input_))))))[0] for i in range(len(input_)))))

print(sum(map(lambda x: 1 if safer(x) else 0, lines)))