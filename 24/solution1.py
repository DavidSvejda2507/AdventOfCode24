import re

# with open("test.txt") as f:
with open("input.txt") as f:
    wires = {}
    gates = []
        
    while True:
        line = f.readline()
        if line == "\n": break
        wires[line[:3]] = int(line[5])
        
    pattern = re.compile(r"(.{3}) ((?:OR)|(?:AND)|(?:XOR)) (.{3}) -> (.{3})")
        
    while True:
        line = f.readline()
        if line == "": break
        line = pattern.match(line).groups()
        gates.append((line[1], line[0], line[2], line[3]))
        
while True:
    waiting_gates = []
    for gate in gates:
        if gate[1] in wires and gate[2] in wires:
            if gate[0] == "OR":
                wires[gate[3]] = 1 if wires[gate[1]] + wires[gate[2]] > 0 else 0
            elif gate[0] == "AND":
                wires[gate[3]] = wires[gate[1]] * wires[gate[2]]
            elif gate[0] == "XOR":
                wires[gate[3]] = (wires[gate[1]] + wires[gate[2]])%2
        else:
            waiting_gates.append(gate)
    if len(gates) == len(waiting_gates):
        break
    gates = waiting_gates
    
z_gates = [x for x in wires if x[0] == "z"]
z_gates.sort(reverse=True)
print(z_gates)
output = 0
for i in z_gates:
    output *= 2
    output += wires[i]
print(output)

  
        
