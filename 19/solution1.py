import re as RE

with open("input.txt") as f:
    targets = []
        
    line = f.readline()
    paterns = line[:-1].split(", ")
    f.readline()
        
    while True:
        line = f.readline()
        if line == "": break
        targets.append(line[:-1])

        
patern = RE.compile(r"^(?:" + "|".join(paterns) + r")*$")

print(sum(map(lambda x: 1 if patern.match(x) != None else 0, targets)))