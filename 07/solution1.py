with open("input.txt") as f:
    lines:list[list[str]] = []
    while(True):
        line = f.readline()
        if (line == ""): break
        line = line.split()
        lines.append((int(line[0][:-1]), list(map(lambda x: int(x), line[1:]))))
        
def solve(target:int, numbers:list[int])->bool:
    if len(numbers) == 1:
        return target == numbers[0]
    product = numbers[0]*numbers[1]
    new_numbers = [numbers[0]+numbers[1]]
    new_numbers.extend(numbers[2:])
    if solve(target, new_numbers): return True
    new_numbers[0] = product
    return solve(target, new_numbers)

print(sum(map(lambda x: x[0] if solve(*x) else 0, lines)))