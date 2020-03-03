from django.shortcuts import render, redirect

from bs4 import BeautifulSoup as BSoup
import requests

from .models import Headline


def scrape(request):
    session = requests.Session()
    session.headers = {
        "User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"
    }
    url = "https://www.theonion.com/latest"

    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    news = soup.find_all('article', {'class': 'js_post_item'})
    for article in news:
        main = article.find_all('div')
        # print(main[-1])
        link = m.get('href') if (m := main[-1].find('a')) else m
        # print("Link", link)
        img_src = a.get('data-srcset').split(' ')[-4] if (a := article.find('img')) else a
        title = t.string if (t := main[-1].find('h2')) else t
        if not title:
            continue
        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = img_src
        new_headline.save()
    return redirect('../')

def new_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, 'news/home.html', context)
