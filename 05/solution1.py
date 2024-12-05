
with open("input.txt") as f:
    rules  = []
    updates = []
    while(True):
        line = f.readline()
        if (line == "\n"): break
        a,b = line.split("|")
        rules.append((int(a), int(b)))
        
    while(True):
        line = f.readline()
        if (line == ""): break
        line = map(lambda x: int(x), line.split(","))
        updates.append(list(line))
    
def checkUpdate(update:list[int], rules):
    for rule in rules:
        try:
            i1 = update.index(rule[0])
            i2 = update.index(rule[1])
        except ValueError:
            continue
        
        if i2<i1:
            return 0
        
    return update[len(update)//2]

print(sum(map(lambda x: checkUpdate(x, rules), updates)))