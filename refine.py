import json
from asm_exporter import asm_exporter, kill_proc
code, proc = asm_exporter(
        proj_pth="~/Code/GhidraProjects/tmp",
        proj_name="tmp",
        bin_pth="~/Code/GhidraProjects/ch14",
        bin_name="exercise03.elf")
# code is a list of ghidra.program.database.code.InstructionDB, proc is the sub-process
# Use code to do any further analysis

try:
    asm_code = dict()
    label = "__MOST__HEAD__"
    asm_code[label] = dict()
    addr_label = dict()
    for line in code:
        inst = str(line)
        addr = str(line.getAddress())
        if line.getLabel():
            print(line.getLabel())
            label = str(line.getLabel())
            asm_code[label] = dict()
            addr_label[addr] = label
        print(line.getAddress(), '\t', inst)
        asm_code[label][addr] = inst

    print("\nRename Destination of Jump \& Call\n")

    for label in asm_code.keys():
        for addr in asm_code[label].keys():
            inst = asm_code[label][addr]
            if inst[-8:] in addr_label:
                inst = inst[:-10] + addr_label[inst[-8:]]
                print(inst)
                asm_code[label][addr] = inst
    with open("/Users/empramsesii/Code/GhidraProjects/ch14/exercise03_s.json", "w") as f:
        json.dump(asm_code, f)

# Terminate the subprocess with proc
finally:
    kill_proc(proc)
