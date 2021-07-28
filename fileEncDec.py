import base64
import logging
import os
import processKiller

def encodeFile(filepath :str,retries=5):
    '''
    encodes a file in base64 with a displacement text, it as filename.ncod
    '''        
    _DISPLACEMENT_TEXT=b"You ARE NOt SuPpOSed To Read ThiS!!"
    _file=None

    for _ in range(0,retries):
        try:
            _file=open(filepath,'r+b')
            _material=_DISPLACEMENT_TEXT+base64.b64encode(_file.read())
            _file.seek(0,0)
            _file.truncate()
            _file.write(_material)
            _file.close()
            os.rename(filepath,filepath+".ncod")
            del _material
            break
        except Exception as e:
            logging.warn("occured {e}")
            _file.close()
            processKiller.killPID(filepath)



def decodeFile(filepath :str,retries=5):
    '''
    decodes a file in base64 with a displacement text, it as filename (removes .ncod)
    '''        
    _DISPLACEMENT_TEXT=b"You ARE NOt SuPpOSed To Read ThiS!!"
    _file=None

    for _ in range(0,retries):
        try:
            _file=open(filepath+".ncod",'r+b')
            _file.seek(len(_DISPLACEMENT_TEXT),0)
            _material=base64.b64decode(_file.read())
            _file.seek(0,0)
            _file.truncate()
            _file.write(_material)
            _file.close()
            del _material
            os.rename(filepath+".ncod",filepath)
            break
        except Exception as e:
            logging.warn("occured {e}")
            _file.close()
            processKiller.killPID(filepath)
