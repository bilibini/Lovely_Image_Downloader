import requests
import json
import re
from bs4 import BeautifulSoup
import cryptocode
from fake_useragent import UserAgent
# import aardio

def getImgSrc_EX(iNumber=1):
    iNumber=int(iNumber)
    url=cryptocode.decrypt('RPmitKoyxkGWT3rNdSIdllrKpBQkM2iXv4Gk*3fceH6rrhEDqRfiurc1k/g==*A/Ria0ZdrIKsY1wDa9zFJQ==*1ehaomVX+IvEYaQ4AtJtSQ==','bilibini')
    head={
        "User-Agent": UserAgent().random
    }
    imgDataList=[]
    imgData={
        'url':'',
        'smallurl':'',
        'title':'小陆离 可爱女孩 可爱 护眼 一手托着下巴的美女壁纸'
    }
    
    res = requests.get(f"{url}/list-{iNumber}.html",headers=head,verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    imgList=soup.select("article > div > div.zhuanti.whitebg.waterfall > ul > li > i > a > img")
    imgSrcList=[img.attrs['src'] for img in imgList]
    return '||'.join(imgSrcList)

def getImgSrc(iNumber=1):
    iNumber=int(iNumber)
    url='http://www.netbian.com/meinv'
    head={
        "User-Agent": UserAgent().random
    }
    imgDataList=[]
    res = requests.get(f"{url}/index_{iNumber}.htm",headers=head,verify=False)
    res.encoding='gbk'
    soup = BeautifulSoup(res.text, 'html.parser')
    imgList=soup.select("#main > div.list > ul > li > a > img")
    for img in imgList:
        imgData={
            'url':'',
            'smallurl':'',
            'title':'小陆离 可爱女孩 可爱 护眼 一手托着下巴的美女壁纸'
        }
        imgData['smallurl']=img.attrs['src']
        imgData['title']=img.attrs['alt']
        imgData['url']=re.findall(r'(.*)small.*',img.attrs['src'])[0]+re.findall(r'.*small([0-9A-Za-z]{11}).*',img.attrs['src'])[0]+'.jpg'
        imgDataList.append(imgData)

    return imgDataList



# print(getImgSrc(2))
