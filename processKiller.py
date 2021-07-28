from sys import path
import psutil
from elevate import elevate
import logging



def killPID(pid):
    logging.debug(f"killing process Id: {pid}")
    if(pid == -1):
        print("Can't Kill Process")
        return
    try:
        psutil.Process(pid).terminate()
    except psutil.NoSuchProcess:
        logging.warn(f"Couldn't kill process with PID {{pid}} REASON: NO SUCH PROCESS")    #TODO warn or debug print
    except Exception as e:
        print(e)



def findPidOfOpenFile(fileName):
    for process in psutil.process_iter():
        try:
            if(fileName in [file.path for file in process.open_files()]):
                return process.pid
        except psutil.AccessDenied:
            continue
    return -1
