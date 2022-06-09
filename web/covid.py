import requests
from bs4 import BeautifulSoup
import os
import django
from django.shortcuts import render

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
django.setup()

from coviddig.models import CovidData

def covid_num():
    req = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=')
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    covid_data = soup.select('td.number')
    data = []
    for dt in covid_data[7::6]:
        data.append(int(dt.text.replace(",","")))
    data.append(max(data)+50000)
    return data
    

if __name__=='__main__':
    i = 0
    while(i<len(covid_num())):
        a = CovidData(co_data = covid_num()[i])
        a.save()
        i += 1