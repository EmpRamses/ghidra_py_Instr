from ghidra_asm_exporter import ghidra_asm_py
from ghidraType import Program

output_pth = ghidra_asm_py(bin_name="exercise03.elf",
                           bin_pth="/Users/empramsesii/Code/GhidraProjects/Struct",
                           output_dir="/Users/empramsesii/Code/GhidraProjects/Struct")

print(output_pth)
prog = Program(name="test")
prog.load_from_file(output_pth)

for key in prog.keys():
    if prog[key].getLabel():
        print(prog[key].getLabel())
    print(key, "\t", prog[key].getInst())
