import itertools as it
import copy

# with open("test.txt") as f:
with open("input.txt") as f:
    codes = []
        
    while True:
        line = f.readline()
        if line == "": break
        codes.append(list(map(lambda x: line[x], range(len(line)-1))))
        
def door_key_pos(key:str):
    if key == "7":
        return (0,0)
    if key == "8":
        return (1,0)
    if key == "9":
        return (2,0)
    if key == "4":
        return (0,1)
    if key == "5":
        return (1,1)
    if key == "6":
        return (2,1)
    if key == "1":
        return (0,2)
    if key == "2":
        return (1,2)
    if key == "3":
        return (2,2)
    if key == "0":
        return (1,3)
    if key == "A":
        return (2,3)
    raise ValueError()

def directional_key_pos(key:str):
    if key == "^":
        return (1,0)
    if key == "<":
        return (0,1)
    if key == "v":
        return (1,1)
    if key == ">":
        return (2,1)
    if key == "A":
        return (2,0)
    raise ValueError()

def move(x, y, step):
    if step == "^":
        return (x,y-1)
    if step == "<":
        return (x-1,y)
    if step == "v":
        return (x,y+1)
    if step == ">":
        return (x+1,y)
    raise ValueError()

def door_keypad(current:tuple, target:tuple):
    x, y = current
    x_, y_ = target
    steps = []
    if x<x_:
        steps.extend([">"]*(x_-x))
    if x>x_:
        steps.extend(["<"]*(x-x_))
    if y<y_:
        steps.extend(["v"]*(y_-y))
    if y>y_:
        steps.extend(["^"]*(y-y_))
    unique = []
    for key, _ in it.groupby(sorted(it.permutations(steps)), "".join):
        x, y = current
        valid = True
        for step in key:
            x, y = move(x, y, step)
            if x==0 and y==3:
                valid = False
        if valid:
            key += "A"
            unique.append(key)
    return unique

def directional_keypad(current:tuple, target:tuple):
    x, y = current
    x_, y_ = target
    steps = []
    if x<x_:
        steps.extend([">"]*(x_-x))
    if x>x_:
        steps.extend(["<"]*(x-x_))
    if y<y_:
        steps.extend(["v"]*(y_-y))
    if y>y_:
        steps.extend(["^"]*(y-y_))
    unique = []
    for key, _ in it.groupby(sorted(it.permutations(steps)), "".join):
        x, y = current
        valid = True
        for step in key:
            x, y = move(x, y, step)
            if x==0 and y==3:
                valid = False
        if valid:
            key += "A"
            unique.append(key)
    return unique

def length1(code, distances):
    current = door_key_pos("A")
    output = 0
    string = ""
    for key in code:
        target = door_key_pos(key)
        if distances[0].get((current, target), -1) == -1:
            inputs = (door_keypad(current, target))
            distances[0][(current, target)] = min(map(lambda x: length2(x, distances), inputs))
        output += distances[0][(current, target)][0]
        string += distances[0][(current, target)][1]
        current = target
    return output, string

def length2(code, distances):
    current = directional_key_pos("A")
    output = 0
    string = ""
    for key in code:
        target = directional_key_pos(key)
        if distances[1].get((current, target), -1) == -1:
            inputs = (directional_keypad(current, target))
            distances[1][(current, target)] = min(map(lambda x: length3(x, distances), inputs))
        output += distances[1][(current, target)][0]
        string += distances[1][(current, target)][1]
        current = target
    return output, string

def length3(code, distances):
    current = directional_key_pos("A")
    output = 0
    string = ""
    for key in code:
        target = directional_key_pos(key)
        if distances[2].get((current, target), -1) == -1:
            inputs = (directional_keypad(current, target))
            distances[2][(current, target)] = min(map(lambda x: (len(x), x), inputs))
        output += distances[2][(current, target)][0]
        string += distances[2][(current, target)][1]
        current = target
    return output, string
    


distances = [{},{},{}]
output = 0
for code in codes:
    length, string = length1(code, distances)
    print(string)
    print(f"{length} * {int(''.join(code[:-1]))}")
    output += int("".join(code[:-1])) * length
print(output)