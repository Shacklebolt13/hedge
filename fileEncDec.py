import base64
import os
import warnings
import processKiller

def encodeFile(filepath :str):        
    try:
        open(filepath+".ncod",'x')
    except FileExistsError:
        pass
    
    with open(filepath,'rb') as file , open(filepath+".ncod",'wb') as writer:
        try:
            writer.write(base64.b64encode(file.read()))
            writer.close()
            file.close()
            print(file.name)
            os.remove(file.name)
        except PermissionError as e:
            processKiller.killPID(processKiller.findPidOfOpenFile(file.name))
            os.remove(file.name)
            warnings.warn("occured {e}")
        except Exception:
            os.remove(writer.name)



def decodeFile(filepath:str):
    try:
        open(filepath,'x')
    except FileExistsError:
        pass
    with open(filepath+".ncod",'rb') as file , open(filepath,'wb') as writer:
        try:
            writer.write(base64.b64decode(file.read()))
            writer.close()
            file.close()
            print(file.name)
            os.remove(file.name)
        except PermissionError as e:
            processKiller.killPID()
            warnings.warn("occured {e}")
        except Exception:
            writer.close()
            os.remove(writer.name)

