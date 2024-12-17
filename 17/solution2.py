import re as RE

with open("input.txt") as f:
    A = int(RE.compile(r"Register A: (\d+)").match(f.readline()).groups()[0])
    B = int(RE.compile(r"Register B: (\d+)").match(f.readline()).groups()[0])
    C = int(RE.compile(r"Register C: (\d+)").match(f.readline()).groups()[0])
    f.readline()
    line = RE.compile(r"Program: ([0-9,]+)").match(f.readline()).groups()[0]
    
    program = list(map(int, line.split(",")))
    

def read_combo(operand, registers):
    if operand < 4:
        return operand
    if operand < 7:
        return registers[operand-4]
    raise ValueError()

def test(A: int):
    registers = [A, B, C]
    pointer = 0
    output = []

    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer+1]
        if opcode == 0:
            registers[0] = registers[0]>>read_combo(operand, registers)
            pointer += 2
        elif opcode == 1:
            registers[1] = registers[1]^operand
            pointer += 2
        elif opcode == 2:
            registers[1] = read_combo(operand, registers)&int(7)
            pointer += 2
        elif opcode == 3:
            if registers[0] == 0:
                pointer += 2
            else:
                pointer = operand
        elif opcode == 4:
            registers[1] = registers[1]^registers[2]
            pointer += 2
        elif opcode == 5:
            if len(output) == len(program):
                return len(output)  
            output.append(read_combo(operand, registers)&int(7))
            if output[-1] != program[len(output)-1]:
                return len(output)-1
            pointer += 2
        elif opcode == 6:
            registers[1] = registers[0]>>read_combo(operand, registers)
            pointer += 2
        elif opcode == 7:
            registers[2] = registers[0]>>read_combo(operand, registers)
            pointer += 2
    
    return len(output)

i=0
step = 1
max_length = 0
prev_solutions = [0]
for target in range(len(program)+1):
    solutions = []
    step = 8**target
    for prev in prev_solutions:
        for i in range(2**11):
            length = test(prev + (step * i))
            if length >= target:
                solutions.append(prev + (step * i))
    
    mask = (8**(target+1))-1
    filtered = []
    for sol in solutions:
        if sol&mask not in filtered:
            filtered.append(sol&mask)
    filtered.sort()
    prev_solutions = filtered
    print(len(prev_solutions))
    
solutions.sort()
print(solutions[0])