import re as RE
import argparse as AP

with open("input.txt") as f:
    A = int(RE.compile(r"Register A: (\d+)").match(f.readline()).groups()[0])
    # A = 216584205979327
    # A = 23070159490669
    # f.readline()
    B = int(RE.compile(r"Register B: (\d+)").match(f.readline()).groups()[0])
    C = int(RE.compile(r"Register C: (\d+)").match(f.readline()).groups()[0])
    f.readline()
    line = RE.compile(r"Program: ([0-9,]+)").match(f.readline()).groups()[0]
    
    program = list(map(int, line.split(",")))
    
parser = AP.ArgumentParser()
parser.add_argument("-A", required=False)
args = parser.parse_args()
if args.A is not None:
    A = int(args.A)
    
registers = [A, B, C]
pointer = 0
output = []

def read_combo(operand, registers):
    if operand < 4:
        return operand
    if operand < 7:
        return registers[operand-4]
    raise ValueError()

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
        output.append(read_combo(operand, registers)&int(7))
        pointer += 2
    elif opcode == 6:
        registers[1] = registers[0]>>read_combo(operand, registers)
        pointer += 2
    elif opcode == 7:
        registers[2] = registers[0]>>read_combo(operand, registers)
        pointer += 2
            
print(*output, sep=",")