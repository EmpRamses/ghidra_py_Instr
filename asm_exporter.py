from ghidra.program.model.listing import Listing
from ghidraType import Inst, Program

args = getScriptArgs()


def bytesToHex(byte):
    hexs = list()
    for b in byte:
        b = (bin(((1 << 8) - 1) & b)[2:]).zfill(8)
        h = hex(int(b, 2))[2:]
        if len(h) == 1:
            h = "0" + h
        hexs.append(h)
    return hexs

cuIterator = Listing.getCodeUnits(currentProgram.getListing(), True)
insts = list()
code = Program(name="test")
for line in cuIterator:
    insts.append(line)
for line in insts:
    label = None
    if line.getLabel():
        label = str(line.getLabel())
    byte = None
    inst = str(line)
    if inst != "?? ??":
        byte = bytesToHex(line.getBytes())

    code.addInst(Inst(
        label,
        str(line.getAddress()),
        inst,
        str(line.getMaxAddress()),
        byte
    ))

code.save_to_file(args[0])
