import requests
import json
# import aardio

def getImgSrc(iNumber=1):
    res = requests.get(f"https://v.api.aa1.cn/api/api-tplist/go.php/api/picture/index?page={iNumber}",verify=False)
    print(res.text)
    data=json.loads(res.text)['data']
    print(data)
    ImgSrclist=['||'.join(pics['pics']) for pics in data]
    return '||'.join(ImgSrclist) 

