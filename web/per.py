import requests
from bs4 import BeautifulSoup
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
django.setup()
from coviddig.models import CovidPer

def covid_per():
    req = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%B1%EC%8B%A0%EC%A0%91%EC%A2%85')
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    covid_data = soup.select('p.info_num')
    data = []
    for dt in covid_data[0:3]:
        data.append(dt.text[0:4])
    return data
    

if __name__=='__main__':
    i = 0
    while(i<len(covid_per())):
        a = CovidPer(co_per = covid_per()[i])
        a.save()
        i += 1