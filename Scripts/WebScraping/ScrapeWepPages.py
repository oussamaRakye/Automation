import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml') # Make xml from the html
quotes = soup.find_all('span', class_='text')   # Get all that are tag span and class text
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

for i in range(len(quotes)):
    print(quotes[i].text)   # Gets rid of the html and only gets the scripts inside
    print('\t' + authors[i].text)   # Gets rid of the html and only gets the scripts inside
    quoteTags = tags[i].find_all('a', class_='tag')
    for tag in quoteTags:
        print(tag.text)
