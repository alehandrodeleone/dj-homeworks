from django.shortcuts import render, redirect
from django.urls import reverse
from bs4 import BeautifulSoup


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    url="https://data.mos.ru/datasets/752"
    response=request.get(url)
    bs=BeautifulSoup(response.text,"html.parser")
    st= bs.findAll('tbody',class_="hasGeodata")
    print(st[0].text)

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
    #     'bus_stations': ...,
    #     'page': ...,
    }
    return render(request, 'stations/index.html', context)
