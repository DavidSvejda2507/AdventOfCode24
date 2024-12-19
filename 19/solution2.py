with open("input.txt") as f:
    targets = []
        
    line = f.readline()
    paterns = line[:-1].split(", ")
    f.readline()
        
    while True:
        line = f.readline()
        if line == "": break
        targets.append(line[:-1])

def match(target: str, paterns: list[str]) -> int:
    counts = [0]*(len(target) + 1)
    counts[len(target)] = 1
    for i in range(len(target)-1, -1, -1):
        for patern in paterns:
            length = len(patern)
            if length + i > len(target):
                continue
            if target[i:i+length] == patern:
                counts[i] += counts[i+length]
    
    return counts[0]

print(sum(map(lambda x: match(x, paterns), targets)))
