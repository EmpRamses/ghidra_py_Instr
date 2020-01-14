# A class of instruction imitating InstructionDB from ghidra

class Inst:
    def __init__(self, label, addr, inst, endaddr):
        self.addr = addr
        self.endaddr = endaddr
        self.inst = inst
        self.label = label
    def getLabel(self):
        return self.rabel
    def getAddress(self):
        return self.addr
    def getEndAddress(self):
        return self.endaddr
    def getInst(self):
        return self.inst
    def getOp(self):
        return self.inst.split(" ", 1)[0]
    def getOpObject(self):
        objs = self.inst.split(" ", 1)[1]
        if "," in objs:
            return objs.split(",")[0]
        else:
            return objs
    def getArgs(self):
        objs = self.inst.split(" ", 1)[1]
        return objs.split(",")
