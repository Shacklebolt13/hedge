import os
import threading
from requests import api
import virustotal3.core
import logging
import time



_API_KEY="3d29cdabf6d196748d9b810412d3494c6ebb7a4972427877a5196bc3ceadf01d"
_vsTotUploader=virustotal3.core.Files(api_key=_API_KEY)
#_FILE=os.path.abspath() FILE TO BE PASSED
_result=False
_info={}
print(_FILE)



def uploadAndStartScan(vsTotUploader: virustotal3.core.Files,filepath):
    uploadId= vsTotUploader.upload(sample=filepath)['data']['id']
    logging.info(uploadId)
    return uploadId



def waitTillCompleted(apiKey,uploadId):
    global _result
    global _info
    _result=False
    statusGetter=threading.Thread(name="statusGetter",target=_getStatus(apiKey,uploadId,2))
    _info=virustotal3.core.get_analysis(apiKey,uploadId)
    waitShow=threading.Thread(name="waitShow",target=_showWaitDialog())
    waitShow.start()
    statusGetter.start()    


def _showWaitDialog():
    global _result
    lst=['/','|','\\','-','/']
    i=0
    while (not _result):
        print("working ",lst[i],end="\r")
        time.sleep(0.1)
        i=(i+1)%5


def _getStatus(apiKey,uploadId,sleep):
    global _result
    global _info
    time.sleep(sleep)
    while not _result:
        info=virustotal3.core.get_analysis(apiKey,uploadId)
        logging.debug(f'{info.keys()}')
        if(info['data']['attributes']['status']=='completed'):
            _result=True
            time.sleep(0.1)
    _info=info['data']['attributes']['stats']
    _showInfo()


def _showInfo():
    global _info
    print(_info)


upid=uploadAndStartScan(_vsTotUploader,_FILE)
print(waitTillCompleted( _API_KEY,upid))