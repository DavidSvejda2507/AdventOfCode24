# with open("test.txt") as f:
with open("input.txt") as f:
    codes = []
        
    while True:
        line = f.readline()
        if line == "": break
        codes.append(int(line[:-1]))
        
        
def iterate(number: int)->int:
    number = (number ^ (number << 6))%16777216
    number = (number ^ (number >> 5))%16777216
    number = (number ^ (number << 11))%16777216
    return number

def iterate_n(number:int, n:int, output:list)->None:
    old_price = number%10
    for i in range(n):
        number = iterate(number)
        new_price = number%10
        output[i] = (new_price-old_price, new_price)
        old_price = new_price
        
def signalize(input:list, output:list)->None:
    for i in range(3,2000):
        output[i] = ((input[i-3][0], input[i-2][0], input[i-1][0], input[i][0]), input[i][1]) 

prices = [None]*2000
signals = [None]*2000
seen = {}
values = {}
for code in codes:
    iterate_n(code, 2000, prices)
    signalize(prices, signals)
    for signal, value in signals[3:]:
        if seen.get(signal, False):
            continue
        seen[signal] = True
        values[signal] = values.get(signal, 0) + value
    for signal, _ in signals[3:]:
        seen[signal] = False

print(max(map(values.get, values.keys())))