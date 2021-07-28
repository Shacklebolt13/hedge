from sys import path
import psutil
from elevate import elevate
import logging



def killPID(pid):
    '''

    finds and kills a process by process id.
    returns True if process was killed successfully, else returns False

    '''
    
    logging.debug(f"killing process Id: {pid}")
    if(pid == -1):
        logging.info("Couldn't kill process with PID {{pid}} REASON: FILE NOT USED BY ANY PROCESS")
        return False
    try:
        psutil.Process(pid).terminate()
        return True
    except psutil.NoSuchProcess:
        logging.warn(f"Couldn't kill process with PID {{pid}} REASON: NO SUCH PROCESS")    #TODO warn or debug print
        return False
    except Exception as e:
        print(e)
        return False



def findPidOfOpenFile(fileName):
    '''

    finds and returns a process' id using the specified file,
    returns -1 if file is not being used by any process or 

    '''

    for process in psutil.process_iter():
        try:
            if(fileName in [file.path for file in process.open_files()]):
                return process.pid
        except psutil.AccessDenied:
            continue
    return -1
