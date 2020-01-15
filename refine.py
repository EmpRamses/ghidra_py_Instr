import json
from asm_exporter import asm_exporter, kill_proc
code = asm_exporter(
        proj_pth="~/repos/GhidraProjects/tmp",
        proj_name="tmp",
        bin_pth="~/repos/GhidraProjects/Struct",
        bin_name="exercise03.elf")
# code is a list of ghidra.program.database.code.InstructionDB, proc is the sub-process
# Use code to do any further analysis

'''
addr_label = dict()
for addr in code.keys():
    if code[addr].getLabel():
        print(code[addr].getLabel())
        label = code[addr].getLabel()
        addr_label[addr] = label
    print(addr, '\t', code[addr].getInst())

print("\nRename Destination of Jump \& Call\n")

for addr in code.keys():
    inst = code[addr].getInst()
    if inst[-8:] in addr_label:
        inst = inst.split(" ")[0] + " " + addr_label[inst[-8:]]
        print(inst)
        code.updateInst(addr, inst)
'''

path = "/home/lcf/repos/GhidraProjects/Struct/exercise03_s.pkl"
code.save_to_file(path)
