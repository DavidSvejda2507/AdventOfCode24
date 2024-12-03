with open("input.txt") as f:
    lines = ""
    while(True):
        line = f.readline()
        if (line == ""): break
        lines+=line
        
import re as RE

regex = RE.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")
matches = regex.findall(lines)
print(matches)

sum = sum(map(lambda x:int(x[0])*int(x[1]), matches))
print(sum)