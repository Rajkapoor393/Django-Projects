from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

# Scrping news from times of india for general news
toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[2:12]  # removing footer links
toi_news = []

for th in toi_headings:
    toi_news.append(th.text)
# Scraping new from forbes for general news
ht_r = requests.get("https://www.forbes.com/")
ht_soup = BeautifulSoup(ht_r.content, 'html.parser')
ht_headings = ht_soup.findAll('a', {'class': 'happening__title'})
ht_headings = ht_headings[0:10]
ht_news = []
for ht in ht_headings:
    ht_news.append(ht.text)

# Scraping news for sports
sport_r = requests.get("https://inshorts.com/en/read/sports")
sport_soup = BeautifulSoup(sport_r.content, 'html.parser')
sport_headings = sport_soup.findAll('span', {'itemprop': 'headline'})
sport_news = []
for news in sport_headings:
    sport_news.append(news.text)

stoi_r = requests.get("https://timesofindia.indiatimes.com/sports")
stoi_soup = BeautifulSoup(stoi_r.content, 'html.parser')
stoi_headings = stoi_soup.findAll('span',{'class':'w_tle'})
stoi_headings = stoi_headings[8:20]
stoi_news = []
for ht in stoi_headings:
    stoi_news.append(ht.text)

# Scraping news for business
busi_r = requests.get("https://inshorts.com/en/read/business")
busi_soup = BeautifulSoup(busi_r.content, 'html.parser')
busi_headings = busi_soup.findAll('span',{'itemprop':'headline'})
busi_news = []
for ht in busi_headings:
    busi_news.append(ht.text)


# Create your views here.
# def index(req):
#     return render(req, 'news/index.html')


def newsbase(req):
    return render(req, 'news_base.html', {'toi_news': toi_news, 'ht_news': ht_news})


def sports(req):
    return render(req, 'sports.html', {'sport_news': sport_news, 'stoi_news': stoi_news})


def business(req):
    return render(req, 'business.html', {'busi_news': busi_news})



