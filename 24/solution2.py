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
        gates.append((line[1], (line[0],line[0]), (line[2],line[2]), (line[3],line[3])))
    
def new_renaming(gates, wires):
    renaming = {}
    for gate in gates:
        renaming[gate[3][0]] = gate[3][0]
    for wire in wires:
        renaming[wire] = wire
    return renaming
    
def rename(gates, renaming):    
    new_gates = []
    for gate in gates:
        new_gates.append((gate[0], (renaming[gate[1][0]], gate[1][1]), (renaming[gate[2][0]], gate[2][1]), (renaming[gate[3][0]], gate[3][1])))
    return new_gates
    
def rename_outputs(gates, renaming):    
    new_gates = []
    for gate in gates:
        new_gates.append((gate[0], (gate[1][0], gate[1][1]), (gate[2][0], gate[2][1]), (renaming[gate[3][0]], renaming[gate[3][1]])))
    return new_gates

def sort_gate_inputs(gates):
    for index, gate in enumerate(gates):
        if gate[2] < gate[1]:
            gates[index] = (gate[0], gate[2], gate[1], gate[3])
   
renaming = new_renaming(gates, wires)
renaming["gqp"] = "z33"
renaming["z33"] = "gqp"
renaming["qgd"] = "z18"
renaming["z18"] = "qgd"
renaming["mwk"] = "z10"
renaming["z10"] = "mwk"
renaming["hsw"] = "jmh"
renaming["jmh"] = "hsw"
# gates = rename_full(gates, renaming)
gates = rename_outputs(gates, renaming)


renaming = new_renaming(gates, wires)
counts = {}
for gate in gates:
    counts[gate[1][0]] = counts.get(gate[1][0], 0) + 1
    counts[gate[2][0]] = counts.get(gate[2][0], 0) + 1
    
for gate in gates:
    if counts.get(gate[3][0], 0) == 0:
        renaming[gate[3][0]] = "Z" + gate[3][0]
gates = rename(gates, renaming)


renaming = new_renaming(gates, wires) 
for gate in gates:
    if (gate[1][0][0] == "y" and gate[2][0][0] == "x") or (gate[1][0][0] == "x" and gate[2][0][0] == "y"):
        assert gate[1][0][1:] == gate[2][0][1:]
        # if gate[1][0][1:] == "24":
        #     print(gate[3])
        if gate[0] == "AND":
            renaming[gate[3][0]] = f"A{gate[1][0][1:]}"
        if gate[0] == "XOR":
            renaming[gate[3][0]] = f"C{gate[1][0][1:]}"
gates = rename(gates, renaming)
sort_gate_inputs(gates)
gates.sort()


renaming = new_renaming(gates, wires) 
for gate in gates:
    if (gate[0] == "OR"):
        if gate[1][0][0] == "A":
            renaming[gate[2][0]] = f"E{gate[1][0][1:]}"
            renaming[gate[3][0]] = f"D{gate[1][0][1:]}"
gates = rename(gates, renaming)
sort_gate_inputs(gates)
gates.sort()

counts = {}
for gate in gates:
    counts[gate[1][0]] = counts.get(gate[1][0], 0) + 1
    counts[gate[2][0]] = counts.get(gate[2][0], 0) + 1
    
for key in counts:
    if counts[key] == 1:
        if key[0] != "A" and key[0] != "E":
            print(key)

print(*gates, sep = "\n")


# Through manual analysing of the printed gates, grepping for specific gates and trial and error I figured out the four swaps
output = ["z33","gqp","z18","qgd","z10","mwk","jmh","hsw"]
output.sort()
print(",".join(output))