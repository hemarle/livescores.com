from django.shortcuts import render
from bs4 import BeautifulSoup as BS
from  urllib.request import Request, urlopen
# Create your views here.

link_raw='https://livescores.com/soccer/{}'

def home(request):
    return render(request, 'base.html')

def scores(request):
    date_raw= request.POST['date']
    link= link_raw.format(date_raw)

    link_req=Request(link, headers={'user-agent':'XYZ-3.0'})
    link_open=urlopen(link_req, timeout=20).read()
    soup= BS(link_open, 'html.parser')

    container=soup.findAll('div',{'class': 'row-gray'})


    total=[]
    for item in container:
        home_team = item.find('div', {'class': 'ply tright name'}).text
        away_team = item.find('div', {'class': 'ply name'}).text
        team_score= item.find('div', {'class': 'sco'}).text
        match_time= item.find('div', {'class': 'min'}).text


        total.append((home_team, away_team, team_score, match_time))

    context={
        'total':total,
        'date': date_raw
    }



    return render(request, 'livescores/scores.html', context)
