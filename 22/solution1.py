# with open("test.txt") as f:
with open("input.txt") as f:
    codes = []
        
    while True:
        line = f.readline()
        if line == "": break
        codes.append(int(line[:-1]))
        
        
def iterate(number: int):
    number = (number ^ (number << 6))%16777216
    number = (number ^ (number >> 5))%16777216
    number = (number ^ (number << 11))%16777216
    return number

def iterate_n(number:int, n:int):
    for _ in range(n):
        number = iterate(number)
    return number

print(sum(map(lambda x: iterate_n(x, 2000), codes)))