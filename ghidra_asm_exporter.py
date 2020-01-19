import os

bin_name = "exercise03.elf"
bin_pth = "/home/lcf/repos/GhidraProjects/Struct"


def ghidra_asm_py(bin_name=bin_name, bin_pth=bin_pth, output_dir=bin_pth):
    output_file = bin_name[:-4] + "_s.pkl"
    output_pth = os.path.join(output_dir, output_file)
    dirn = os.path.dirname(os.path.abspath(__file__))
    os.system("sh " + dirn + "/ghidra_exporter.sh" + " -n " + bin_name + " -b " + bin_pth + " -o " + output_pth)
    return output_pth

