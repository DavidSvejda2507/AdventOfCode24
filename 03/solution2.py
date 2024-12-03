with open("input.txt") as f:
    lines = ""
    while(True):
        line = f.readline()
        if (line == ""): break
        lines+=line
        
import re as RE

regex = RE.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do)\(\)|(don't)\(\)")
matches = regex.findall(lines)
print(matches)

sum = 0
enabled = True
for match in matches:
    if match[3]=="don't":enabled = False
    elif match[2]=="do":enabled = True
    else:
        if enabled:
            sum += int(match[0])*int(match[1])

print(sum)