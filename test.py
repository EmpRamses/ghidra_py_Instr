from asm_exporter import asm_exporter, kill_proc
code, proc = asm_exporter(
        proj_pth=~/Code/GhidraProjects/tmp,
        proj_name=tmp,
        bin_pth=~/Code/GhidraProjects,
        bin_name=link_3.elf)
# code is a list of ghidra.program.database.code.InstructionDB, proc is the sub-process
# Use code to do any further analysis


# Terminate the subprocess with proc
kill_proc(proc)
