import requests
from bs4 import BeautifulSoup

urlT = 'https://scrapingclub.com/exercise/list_basic/'


def searching(count, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')  # Make xml from the html
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print('{}) Price: {}, item name: {}'.format(count, itemPrice, itemName))
        count+=1

    pages = soup.find('ul', class_='pagination')
    links = pages.find_all('a', class_='page-link')
    for link in links:
        if (link.text=='Next'):
            x = link.get('href')
            searching(count, urlT+x)


count = 1
searching(count, urlT)
