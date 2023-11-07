import requests
import json
import re
from bs4 import BeautifulSoup
import cryptocode
import random
from fake_useragent import UserAgent
# import aardio

def getImgSrc_EX(iNumber=1):
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

def getimgList_1(iNumber=2):
    iNumber=int(iNumber)+1
    imgjsonlist=[]
    def get(url):
        head={
            "User-Agent": UserAgent().random
        }
        res = requests.get(url,headers=head,verify=False)
        res.encoding='gbk'
        soup = BeautifulSoup(res.text, 'html.parser')
        imgList=soup.select("#main > div.list > ul > li > a > img")
        imgDataList=[]
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
    try:
        url1=f'http://www.netbian.com/meinv/index_{iNumber}.htm'
        url2=f'http://www.netbian.com/shouji/meinv/index_{iNumber}.htm'
        imgjsonlist=get(url1)+get(url2)
    except:
        imgjsonlist=[{
            'url':'err.png',
            'smallurl':'err.png',
            'title':'数据加载错误'
        }]
    return imgjsonlist

def getimgList_2(iNumber=1):
    iNumber=int(iNumber)
    imgjsonlist=[]
    def get(url):
        head={
            "user-agent": UserAgent().random
        }
        res = requests.get(url,headers=head,stream=True,timeout=(5,5),verify=False)
        soup = BeautifulSoup(res.text, 'html.parser')
        imgList=soup.select("main div div section ul li div a img")
        imgDataList=[]
        for img in imgList:
            imgData={
                'url':'',
                'smallurl':'',
                'title':'小陆离 可爱女孩 可爱 护眼 一手托着下巴的美女壁纸'
            }
            imgData['smallurl']=img.attrs['src']
            imgData['title']=img.attrs['alt']
            imgData['url']=img.attrs['src'].split('?x-oss')[0]
            imgDataList.append(imgData)
        return imgDataList
    try:
        url1=f'https://bizhi.cheetahfun.com/sj/c3j/p{iNumber}'
        url2=f'https://bizhi.cheetahfun.com/dn/c3j/p{iNumber}'
        imgjsonlist=get(url1)+get(url2)
    except :
        imgjsonlist=[{
            'url':'err.png',
            'smallurl':'err.png',
            'title':'数据加载错误'
        }]
    return imgjsonlist

def getSearchImgSrc(text='黑丝',iNumber=1):
    iNumber=int(iNumber)
    imgjsonlist=[]
    def get(url):
        head={
            "user-agent": UserAgent().random
        }
        res = requests.get(url,headers=head,stream=True,timeout=(5,5),verify=False)
        soup = BeautifulSoup(res.text, 'html.parser')
        imgList=soup.select("main div section ul li div a")
        imgDataList=[]
        for img in imgList:
            imgData={
                'url':'',
                'smallurl':'',
                'title':'小陆离 可爱女孩 可爱 护眼 一手托着下巴的美女壁纸'
            }
            img.select('img')
            if len(img.select('img'))==0:
                continue
            elif len(img.select('img'))==1:
                img=img.select('img')[0]
            else:
                img=img.select('img')[1]
            imgData['smallurl']=img.attrs['src']
            imgData['title']=img.attrs['alt']
            imgData['url']=img.attrs['src'].split('?x-oss')[0]
            imgDataList.append(imgData)
        return imgDataList
    try:
        url1=f'https://bizhi.cheetahfun.com/search.html?search={text}&page={iNumber}'
        url2=f'https://bizhi.cheetahfun.com/sj/search.html?search={text}&page={iNumber}'
        imgjson=get(url1)+get(url2)
        random.shuffle(imgjson)
    except:
        imgjson=[{
            'url':'err.png',
           'smallurl':'err.png',
            'title':'数据加载错误'
        }]
    return imgjson

def getImgSrc(iNumber=1):
    iNumber=int(iNumber)
    imgDataList=getimgList_1(iNumber)+getimgList_2(iNumber)
    random.shuffle(imgDataList)

    return imgDataList



# print(getSearchImgList())

