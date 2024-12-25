import itertools as it

# with open("test.txt") as f:
with open("input.txt") as f:
    cases = []
    
    while True:
        line = f.readline()
        if line == "": break
        case = line[:-1]
        for _ in range(6):
            case += f.readline()[:-1]
        f.readline()
        val = 0
        for char in case:
            val *= 2
            if char == "#":
                val += 1
                
        cases.append(val)

    
def test(tuple):
    if tuple[0] & tuple[1] != 0:
        return 0
    return 1
    
print(sum(map(test, it.combinations(cases, 2))))