from asm_exporter import asm_exporter, kill_proc
code, proc = asm_exporter(
        proj_pth="~/Code/GhidraProjects/tmp",
        proj_name="tmp",
        bin_pth="~/Code/GhidraProjects/ch14",
        bin_name="exercise03.elf")
# code is a list of ghidra.program.database.code.InstructionDB, proc is the sub-process
# Use code to do any further analysis

try:
    with open("/Users/empramsesii/Code/GhidraProjects/ch14/exercise03.s", "w") as f:
        for line in code:
            if line.getLabel():
                print(line.getLabel())
                f.write(str(line.getLabel()) + '\n')
            print(line.getAddress(), '\t', line)
            f.write(str(line.getAddress()) + '\t' + str(line) + '\n')

# Terminate the subprocess with proc
finally:
    kill_proc(proc)
