from sys import path
import psutil
from elevate import elevate

def killPID(pid):
    if(pid == -1):
        print("Can't Kill Process")
    try:
        psutil.Process(pid).terminate()
    except psutil.NoSuchProcess:
        pass    #TODO warn or debug print


def findPidOfOpenFile(fileName):
    for process in psutil.process_iter():
        try:
            if(fileName in [file.path for file in process.open_files()]):
                return process.pid
        except psutil.AccessDenied:
            continue
    return -1

print(findPidOfOpenFile("ss"))
#elevate(show_console=False)
print("ss")