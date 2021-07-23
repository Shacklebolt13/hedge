import os
import virustotal3.core
import json
API_KEY="3d29cdabf6d196748d9b810412d3494c6ebb7a4972427877a5196bc3ceadf01d"

vst=virustotal3.core.Files(api_key=API_KEY)
scanRes= virustotal3.core.Files.upload(vst,'fileEncDec.py')['data']['id']
print(scanRes,virustotal3.core.base64.b64decode(scanRes))
info=virustotal3.core.get_analysis(vst.api_key,scanRes)
print(info)