with open("input.txt") as f:
# with open("test.txt") as f:
    lines = ""
    while(True):
        line = f.readline()
        if (line == ""): break
        lines+=line

length = 10
import re as RE


regex1 = RE.compile(r"XMAS")
regex2 = RE.compile(r"SAMX")
regex3 = RE.compile(r"X(?s:.){139}M(?s:.){139}A(?s:.){139}S")
regex4 = RE.compile(r"X(?s:.){140}M(?s:.){140}A(?s:.){140}S")
regex5 = RE.compile(r"X(?s:.){141}M(?s:.){141}A(?s:.){141}S")
regex6 = RE.compile(r"S(?s:.){139}A(?s:.){139}M(?s:.){139}X")
regex7 = RE.compile(r"S(?s:.){140}A(?s:.){140}M(?s:.){140}X")
regex8 = RE.compile(r"S(?s:.){141}A(?s:.){141}M(?s:.){141}X")

matches = 0
regexes:list[RE.Pattern] = [regex1,regex2,regex3,regex4,regex5,regex6,regex7,regex8]
for regex in regexes:
    print(regex.findall(lines))
    start = 0
    running = True
    while running:
        match_ = regex.search(lines, start)
        print(match_)
        if match_ is None:
            running = False
        else:
            matches += 1
            start = match_.start()+1
    print(matches)            
