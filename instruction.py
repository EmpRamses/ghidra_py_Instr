# A class of instruction imitating InstructionDB from ghidra

class Inst:
    def __init__(self, label, addr, inst, endaddr):
        self.addr = addr
        self.endaddr = endaddr
        self.inst = inst
        self.label = label
    def getLabel():
        return self.rabel
    def getAddress():
        return self.addr
    def getEndAddress():
        return self.endaddr
    def getInst():
        return self.inst
    def getOp():
        return self.inst.split(" ", 1)[0]
    def getOpObject():
        objs = self.inst.split(" ", 1)[1]
        if "," in objs:
            return objs.split(",")[0]
        else:
            return objs
    def getArgs():
        objs = self.inst.split(" ", 1)[1]
        return objs.split(",")
