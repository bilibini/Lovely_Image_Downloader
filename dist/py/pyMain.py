import requests
import json
from bs4 import BeautifulSoup
import cryptocode
from fake_useragent import UserAgent
# import aardio

def getImgSrc(iNumber=1):
    iNumber=int(iNumber)
    url=cryptocode.decrypt('RPmitKoyxkGWT3rNdSIdllrKpBQkM2iXv4Gk*3fceH6rrhEDqRfiurc1k/g==*A/Ria0ZdrIKsY1wDa9zFJQ==*1ehaomVX+IvEYaQ4AtJtSQ==','bilibini')
    head={
        "User-Agent": UserAgent().random
    }
    res = requests.get(f"{url}/list-{iNumber}.html",headers=head,verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    imgList=soup.select("article > div > div.zhuanti.whitebg.waterfall > ul > li > i > a > img")
    imgSrcList=[img.attrs['src'] for img in imgList]
    return '||'.join(imgSrcList)

# print(getImgSrc(1))