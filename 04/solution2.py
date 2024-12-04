
with open("input.txt") as f:
# with open("test.txt") as f:
    lines = ""
    while(True):
        line = f.readline()
        if (line == ""): break
        lines+=line

import re as RE

regex1 = RE.compile(r"M(?s:.)M(?s:.){139}A(?s:.){139}S(?s:.)S")
regex2 = RE.compile(r"M(?s:.)S(?s:.){139}A(?s:.){139}M(?s:.)S")
regex3 = RE.compile(r"S(?s:.)S(?s:.){139}A(?s:.){139}M(?s:.)M")
regex4 = RE.compile(r"S(?s:.)M(?s:.){139}A(?s:.){139}S(?s:.)M")

# regex1 = RE.compile(r"M(?s:.)M(?s:.){9}A(?s:.){9}S(?s:.)S")
# regex2 = RE.compile(r"M(?s:.)S(?s:.){9}A(?s:.){9}M(?s:.)S")
# regex3 = RE.compile(r"S(?s:.)S(?s:.){9}A(?s:.){9}M(?s:.)M")
# regex4 = RE.compile(r"S(?s:.)M(?s:.){9}A(?s:.){9}S(?s:.)M")


matches = 0
regexes:list[RE.Pattern] = [regex1,regex2,regex3,regex4]
for regex in regexes:
    start = 0
    running = True
    while running:
        match_ = regex.search(lines, start)
        if match_ is None:
            running = False
        else:
            matches += 1
            start = match_.start()+1
    print(matches)            
