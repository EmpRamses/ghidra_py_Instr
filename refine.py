import json
from asm_exporter import asm_exporter, kill_proc
code = asm_exporter(
        proj_pth="~/repos/GhidraProjects/tmp",
        proj_name="tmp",
        bin_pth="~/repos/GhidraProjects/Struct",
        bin_name="exercise03.elf")
# code is a list of ghidra.program.database.code.InstructionDB, proc is the sub-process
# Use code to do any further analysis

asm_code = dict()
addr_label = dict()
for line in code:
    inst = line.getInst()
    addr = line.getAddress()
    if line.getLabel():
        print(line.getLabel())
        label = line.getLabel()
        addr_label[addr] = label
    print(line.getAddress(), '\t', inst)
    asm_code[addr] = inst

print("\nRename Destination of Jump \& Call\n")

for addr in asm_code.keys():
    inst = asm_code[addr]
    if inst[-8:] in addr_label:
        inst = inst.split(" ")[0] + " " + addr_label[inst[-8:]]
        print(inst)
        asm_code[addr] = inst
with open("~/repos/GhidraProjects/Struct/exercise03_s.json", "w") as f:
    addr_label = dict(zip(addr_label.values(), addr_label.keys()))
    code_dict = {**asm_code, **addr_label}
    json.dump(code_dict, f)
