import ghidra_bridge
import os
import sys
import time
import signal
import warnings
import subprocess
import socket

def is_use(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('127.0.0.1', int(port)))
        s.shutdown(2)
        return True
    except Exception as e:
        return False

def serve_detect(port=4768):
    for _ in range(300):
        if is_use(port):
            return True
        time.sleep(0.1)
    print("Time Out")
    sys.exit()

# Choose any argument you need & Delete other arguments
def asm_exporter(proj_pth, proj_n, bin_pth, bin_n):
    code = list()
    # Modify the command as arguments you chosen above
    proc = subprocess.Popen(["nohup", "./ghidra_bridge.sh", "-n", bin_n, "-p", proj_pth, "-b", bin_pth, "-m", proj_n], preexec_fn=os.setsid)
    serve_detect()
    with ghidra_bridge.GhidraBridge(namespace=globals()):
        Listing = ghidra.program.model.listing.Listing
        cuIterator = Listing.getCodeUnits(currentProgram.getListing(), True)
        for line in cuIterator:
            code.append(line)
    return code, proc        # code is a list of ghidra.program.database.code.InstructionDB, proc is the sub-process

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
