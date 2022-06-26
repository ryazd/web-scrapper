import string
import os
import requests
from bs4 import BeautifulSoup


num_of_page = int(input())
type_article = input()
for i in range(num_of_page):
    url = f'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={i + 1}'
    req = requests.get(url)
    os.mkdir(f'Page_{i + 1}')
    if req:
        soup = BeautifulSoup(req.content, 'html.parser')
        article = soup.find_all('article')
        article = [i for i in article if f"\n{type_article}\n" in i.find('span', {'data-test': 'article.type'}).text]
        names = [i.find('a').text for i in article]
        for j in range(len(names)):
            names[j] = names[j].rstrip(string.punctuation)
            names[j] = names[j].replace(" — ", "—")
            names[j] = names[j].replace(" ", "_")
        for k in range(len(names)):
            with open(f'Page_{i + 1}/{names[k]}.txt', "w", encoding="UTF-8") as file:
                req1 = requests.get("https://www.nature.com" + article[k].find('a').get('href')).content
                soup1 = BeautifulSoup(req1, "html.parser")
                t = soup1.find('div', {'class': "c-article-body u-clearfix"}).text
                file.write(t)
    else:
        print("Invalid movie page!")