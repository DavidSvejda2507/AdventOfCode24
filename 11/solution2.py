with open("input.txt") as f:
    
    l = f.readline()
    line={}
    for i in l.split():
        line[i] = 1
    
        
def update(line):
    output = {}
    for key in line:
        val = line.get(key)
        if key == "0":
            output["1"] = output.get("1", 0) + val
        elif len(key) % 2 == 0:
            new_key = key[:len(key)//2]
            output[new_key] = output.get(new_key, 0) + val
            new_key = str(int(key[len(key)//2:]))
            output[new_key] = output.get(new_key, 0) + val
        else:
            new_key = str(2024*int(key))
            output[new_key] = output.get(new_key, 0) + val
    return output

# print(line)
for i in range(75):
    print(i)
    line = update(line)
    # print(line)
print(sum(map(lambda x:line[x], line)))
