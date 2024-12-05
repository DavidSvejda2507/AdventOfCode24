
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
            return fixOrdering(update, rules)
        
    return 0

def fixOrdering(update:list[int], rules:list[tuple[int, int]]):
    rules = list(filter(lambda x: (x[0] in update) & (x[1] in update), rules))
    update = sorted(update, key=lambda x: sum(map(lambda y:1 if x==y[0] else 0, rules)))
    return update[len(update)//2]

print(sum(map(lambda x: checkUpdate(x, rules), updates)))