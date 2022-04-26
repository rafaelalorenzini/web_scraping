from bs4 import BeautifulSoup
import requests
import random
import re
import locale

def get_item_price(agent, link):
    headers = {"User-Agent": "{agent}".format(agent=agent)}
    response = requests.get(link, headers=headers).text


    bs = BeautifulSoup(response, "html.parser")

    data = bs.find('div', class_='sh-dgr__content')

    print(agent)
    preco = data.find('span', class_='a8Pemb').text

    preco = re.sub("[^0-9.,]", "", preco)
    print(preco)
    return preco


def get_location(country, search):
    if country == 'cr':
        url = 'https://www.google.co.cr/search?q={search}&oq={search}&uule=w+CAIQICIKQ29zdGEgUmljYQ&hl=es&gl=cr&tbm=shop&sourceid=chrome&ie=UTF-8'.format(
            search=search)
        locale.setlocale(locale.LC_ALL, 'es_CR.UTF8')
    elif country == 'br':
        url = 'https://www.google.com.br/search?q={search}&oq={search}&tbm=shop&uule=w+CAIQICIGQnJhemls&hl=pt&gl=br&sourceid=chrome&ie=UTF-8'.format(
            search=search)
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF8')
    elif country == 'ar':
        url = 'https://www.google.com.ar/search?q={search}&oq={search}&uule=w+CAIQICIJQXJnZW50aW5h&hl=es&gl=ar&tbm=shop&sourceid=chrome&ie=UTF-8'.format(
            search=search)
        locale.setlocale(locale.LC_ALL, 'es_ar.UTF8')
    elif country == 'co':
        url = 'https://www.google.com.co/search?q={search}&oq={search}&tbm=shop&uule=w+CAIQICIWQm9nb3RhLEJvZ290YSxDb2xvbWJpYQ&hl=es&gl=co&sourceid=chrome&ie=UTF-8'.format(
            search=search)
        locale.setlocale(locale.LC_ALL, 'es_CO.UTF8')
    elif country == 'uy':
        url = 'https://www.google.com.uy/search?q={search}&oq={search}&hl=es&gl=uy&tbm=shop&sourceid=chrome&ie=UTF-8'.format(
            search=search)
        locale.setlocale(locale.LC_ALL, 'es_UY.UTF8')
    elif country == 'pe':
        url = 'https://www.google.com.pe/search?q={search}&oq={search}&uule=w+CAIQICIEUGVydQ&hl=es&gl=pe&tbm=shop&sourceid=chrome&ie=UTF-8'.format(
            search=search)
        locale.setlocale(locale.LC_ALL, 'es_PE.UTF8')
    elif country == 'ec':
        url = 'https://www.google.com.ec/search?q={search}&oq={search}&uule=w+CAIQICIHRWN1YWRvcg&hl=es&gl=ec&tbm=shop&sourceid=chrome&ie=UTF-8'.format(
            search=search)
        locale.setlocale(locale.LC_ALL, 'es_EC.UTF8')
    elif country == 'cl':
        url = 'https://www.google.cl/search?q={search}&oq={search}&uule=w+CAIQICIFQ2hpbGU&hl=es&gl=cl&tbm=shop&sourceid=chrome&ie=UTF-8'.format(
            search=search)
        locale.setlocale(locale.LC_ALL, 'es_CL.UTF8')
    elif country == 'mx':
        url = 'https://www.google.com.mx/search?q={search}&oq={search}&uule=w+CAIQICIGTWV4aWNv&hl=es&gl=mx&tbm=shop&sourceid=chrome&ie=UTF-8'.format(
            search=search)
        locale.setlocale(locale.LC_ALL, 'es_MX.UTF8')
    return url

agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3198.0 Safari/537.36 OPR/49.0.2711.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39']

link = get_location('br', 'Iphone 1')
print(link)
locale.atof(get_item_price(random.choice(agents), link))