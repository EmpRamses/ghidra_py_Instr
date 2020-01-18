# A class of instruction imitating InstructionDB from ghidra
import os
import pickle

class Inst:
    def __init__(self, label, addr, inst, endaddr, byte):
        self.addr = addr
        self.endaddr = endaddr
        self.inst = inst
        self.label = label
        self.byte = byte

    def getLabel(self):
        return self.label

    def getAddress(self):
        return self.addr

    def getEndAddress(self):
        return self.endaddr

    def getInst(self):
        return self.inst

    def updateInst(self, inst):
        self.inst = inst

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

    def getSrc(self):
        return self.getArgs()[1]

    def getBytes(self):
        return self.byte


class Program:
    def __init__(self, name):
        self.name = name
        self.insts = dict()

    def __getitem__(self, key):
        return self.insts[key]

    def addInst(self, inst):
        self.insts[inst.getAddress()] = inst
        if inst.getLabel():
            self.insts[inst.getLabel()] = inst

    def addInsts(self, insts):
        for inst in insts:
            self.addInst(inst)

    def updateInst(self, addr, instr):
        self.insts[addr].updateInst(instr)

    def keys(self):
        return self.insts.keys()

    def save_to_file(self, path):
        dirn = os.path.dirname(path)
        if not os.path.isdir(dirn):
            os.makedirs(dirn)
        with open(path, "wb") as f:
            pickle.dump(self.insts, f)

    def load_from_file(self, path):
        try:
            with open(path, "rb") as f:
                self.insts = pickle.load(f, encoding="iso-8859-1")
        except OSError as ose:
            print("No Such File")


