import requests
from bs4 import BeautifulSoup
import json

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')
quotes_dict = []

for i in range(0, len(quotes)):
    lis = []
    tagsforquote = tags[i].find_all('a', class_='tag')
    for tagforquote in tagsforquote:
        lis.append(tagforquote.text)
    dic2 = {'tags': lis, 'author': authors[i].text, 'quote': quotes[i].text}
    quotes_dict.append(dic2)

with open('qoutes.json', 'w', encoding='utf-8') as fl:
    json.dump(quotes_dict, fl, ensure_ascii=False)

quotess = soup.select('.quote')
authors_info = []
for quote in quotess:
    author_url = url + quote.select_one('a')['href']
    author_page = requests.get(author_url)
    author_soup = BeautifulSoup(author_page.text, 'lxml')
    name = author_soup.find('h3', class_='author-title')
    date = author_soup.find('span', class_='author-born-date')
    location = author_soup.find('span', class_='author-born-location')
    description = author_soup.find('div', class_='author-description')
    dic2 = {'fullname': name.text, 'born-date': date.text, 'born-location': location.text, 'description': description.text.strip()}
    authors_info.append(dic2)

with open('authors.json', 'w', encoding='utf-8') as fl:
    json.dump(authors_info, fl, ensure_ascii=False)







