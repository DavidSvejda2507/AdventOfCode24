with open("input.txt") as f:
    while(True):
        l = f.readline()
        if (l == ""): break
        line=l.split()
        
def update(line):
    output = []
    for ele in line:
        if ele == "0":
            output.append("1")
        elif len(ele) % 2 == 0:
            output.append(ele[:len(ele)//2])
            output.append(str(int(ele[len(ele)//2:])))
        else:
            output.append(str(2024*int(ele)))
    return output

# print(line)
for i in range(25):
    line = update(line)
    # print(line)
print(len(line))
