import ghidra_bridge
import os
import sys
import time
import signal
import warnings
import subprocess
import socket
import traceback
from tqdm import tqdm
from instruction import Inst, Program

def is_use(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('127.0.0.1', int(port)))
        s.shutdown(2)
        return True
    except Exception as e:
        return False

def serve_detect(port=4768):
    print("Waiting for Server")
    for _ in tqdm(range(300), desc="Waiting" , total=300):
        if is_use(port):
            time.sleep(0.1)
            return True
        time.sleep(0.1)
    print("Time Out")
    sys.exit()

# Choose any argument you need & Delete other arguments
def asm_exporter(proj_pth, proj_name, bin_pth, bin_name):
    code = Program(bin_name)
    insts = list()
    # Modify the command as arguments you chosen above
    dirn = os.path.dirname(os.path.abspath(__file__))
    proc = subprocess.Popen(["nohup", dirn + "/ghidra_bridge.sh", "-n", bin_name, "-p", proj_pth, "-b", bin_pth, "-m", proj_name], preexec_fn=os.setsid)
    serve_detect()
    try:
        with ghidra_bridge.GhidraBridge(namespace=globals()):
            Listing = ghidra.program.model.listing.Listing
            cuIterator = Listing.getCodeUnits(currentProgram.getListing(), True)
            for line in cuIterator:
                insts.append(line)
            for line in tqdm(insts, total=len(insts)):
                label = None
                if line.getLabel():
                    label = str(line.getLabel())
                code.addInst(Inst(
                    label,
                    str(line.getAddress()),
                    str(line),
                    str(line.getMaxAddress())
                    ))
    finally:
        kill_proc(proc)
    return code       # code is an object of Program

# Use to terminate all processes created by subprocess
def kill_proc(proc):
    proc.terminate()
    proc.wait()

    try:
        os.killpg(proc.pid, signal.SIGTERM)
        return True
    except OSError as e:
        warnings.warn(e)
        return False
