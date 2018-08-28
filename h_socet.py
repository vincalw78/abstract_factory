from bs4 import BeautifulSoup
import requests
from lxml import html


def ex_1(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.title.text)

    tree = html.fromstring(response.content)
    r = tree.xpath('//*[@id="contForSide"]/div[3]/div/ul[2]/li')
    l = [lr.text for lr in r]
    print(l)


# 3
def ex_3():
    response = requests.get('https://www.leboncoin.fr/locations/offres/reunion/?th=1&parrot=0')






if __name__ == '__main__':
    ex_1('https://lviv.itea.ua/courses-itea/python/python-advanced/')