from django.shortcuts import render
from .models import CovidData
from .models import CovidPer
from .models import DailyCovid

# Create your views here.
def main_page(request):
    covidnum = CovidData.objects.all()
    covidper = CovidPer.objects.all()   
    dailyco = DailyCovid.objects.all()
    
    covid = {"서울":covidnum[0], "부산":covidnum[1], "대구":covidnum[2],
    "인천":covidnum[3], "광주":covidnum[4], "대전":covidnum[5], "울산":covidnum[6],
    "세종":covidnum[7], "경기":covidnum[8], "강원":covidnum[9], "충북":covidnum[10],
    "충남":covidnum[11], "전북":covidnum[12], "전남":covidnum[13], "경북":covidnum[14],
    "경남":covidnum[15], "제주":covidnum[16], "최대값":covidnum[18], "1차":covidper[0],
    "2차":covidper[1], "3차":covidper[2], "날짜1":dailyco[0], "날짜2":dailyco[1], "날짜3":dailyco[2],
    "날짜4":dailyco[3], "날짜5":dailyco[4], "날짜6":dailyco[5], "날짜7":dailyco[6]}

    return render(request, "main.html", covid)

def circle(request):
    covidper = CovidPer.objects.all()   
    covid = {"1차":covidper[0], "2차":covidper[1], "3차":covidper[2]}
    return render(request, "circle.html", covid)

def 마스크착용시도별(request):
    return render(request, "마스크착용시도별.html")

def vaccine1(request):
    return render(request, "백신_1.html")