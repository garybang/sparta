import requests, re
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('mongodb://admin_gary:bang9476141!@13.125.251.5', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbEx

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.neolook.com/archives',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

exIDs=soup.select('ul.items:nth-of-type(n+3):nth-of-type(-n+6) > li')

for exID in exIDs:
    tempID=exID.select_one('a')['href'].split('/')[2]
    exPlace=exID.select_one('a > span').text.split('@')[1].strip()

    dataID = requests.get('https://www.neolook.com/archives/'+tempID,headers=headers)
    #print(tempID)
    soupID = BeautifulSoup(dataID.text, 'html.parser')
    
    exTitle = soupID.select_one('div.description > div > h1')
    if exTitle == None:
        exTitle = soupID.select_one('div.description > div > h2 > span')
        if exTitle == None:
            exTitle = soupID.select_one('div.description > div > h2')
    exTitle=exTitle.text
    
    exImg = 'https://www.neolook.com/archives/'+tempID[:-1]+'01'+tempID[-1:]+'.jpg'
    exDate=soupID.select_one('div.description > div > h2 > span:nth-child(3)')
    if exDate == None:
       exDate = soupID.select_one('div.description > div > h2')
    if exDate.text.strip() == '':
        exDate = soupID.select_one('div.description > div > h2 > span:nth-child(4)')
    if not exDate.text.strip()[0].isdigit():
        exDate = soupID.select_one('div.description > div > h2:nth-child(2)')
    
    exOpen=exDate.text.strip().split('▶︎')[0]
    exClose=exDate.text.strip().split('▶︎')[1].strip()[:9]
    if not exClose[1].isdigit():
        exClose=''
    
    exOpen_year=exOpen[:4]
    exOpen_month=exOpen[5:7]
    exOpen_day=exOpen[7:]
    
    exClose_year=exClose[:4]
    exClose_month=exClose[5:7]
    exClose_day=exClose[7:]

    doc = {
        'exID': tempID,
        'exTitle': exTitle,
        'exImg' : exImg,
        'exPlace':exPlace,
        'exOpen_year':exOpen_year,
        'exOpen_month': exOpen_month,
        'exOpen_day': exOpen_day,
        'exClose_year': exClose_year,
        'exClose_month': exClose_month,
        'exClose_day': exClose_day,
    }
    db.exDB.insert_one(doc)