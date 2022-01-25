import numpy as np
from links_sheets import web_amazon
import pandas as pd
import requests
import regex as re
from bs4 import BeautifulSoup
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from functions import timezones
sys.path.insert(0,'chromedriver.exe')
options = Options()
options.add_argument('-headless')

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

def explode_str(df, col, sep):
    s = df[col]
    i = np.arange(len(s)).repeat(s.str.count(sep) + 1)
    return df.iloc[i].assign(**{col: sep.join(s).split(sep)})

def web_scraping(sheet):
    
    links_sheet = web_amazon(sheet)
    df_final=pd.DataFrame()
    links_final = []
    for link in links_sheet['links']:
        print(link)
        page_link = requests.get(link, headers=HEADERS)

        html_contents_link = page_link.content
        soup_link = BeautifulSoup(html_contents_link, features="lxml")
        try:
            results_link = soup_link.find_all('a', {'class': "a-link-normal s-no-outline"})
            link_amazon = []
            for result in results_link:
                try:
                    if result is not None:
                        result1 = result.attrs['href']
                        link = 'https://www.amazon.com.br' + result1
                        link_amazon.append(link)

                except AttributeError:
                        pass

            links_final.append(link_amazon)

        except:
            pass


    links_final = [item for sublist in links_final for item in sublist]

    print(len(link_amazon))
    link_amazon = list(dict.fromkeys(links_final))
    print(len(link_amazon))

    df = pd.DataFrame()

    for link in link_amazon:
        print(link)
        try:
            browser = webdriver.Chrome('chromedriver')
            browser.get(link)
            soup_amazon = BeautifulSoup(browser.page_source, 'html.parser')

            try:
                title = soup_amazon.find(id='productTitle').get_text().strip()
            except:
                title = soup_amazon.find('span', {'id': "productTitle"}).get_text().strip()


            try:
                price = float(soup_amazon.find('span',{'class':"a-offscreen"}).get_text().replace('.','').replace('R$','').replace(',','.').strip())
            except:
                price = ''

            results_amazon = soup_amazon.find_all('td', {'class': "a-size-base prodDetAttrValue"})

            for result in results_amazon:
                if re.findall(r'[0-9]{10,}', result.get_text().strip()):
                    data = re.findall(r'[0-9]{10,}', result.get_text().strip())
                else:
                    data = re.findall(r'[a-zA-Z0-9]{10,}', result.get_text().strip())
                if data:
                    ean = str(data)

            current_time = timezones.country_current_time('br')
            inserts = [{
                'product_name': title,
                'product_price': price,
                'ean': ean,
                'country': 'br',
                'time': current_time
                }]
            inserts = pd.DataFrame(inserts)

            df = df.append(inserts, ignore_index=True)
            df = df[df.product_price != '']
            df = df[df.ean != '']
            print(df)
        except:
            pass



    df_final = df_final.append(df, ignore_index=True)
    df_final['ean'] = df_final['ean'].str.replace(r"[", "", regex=True).str.replace(r"]", "", regex=True).str.replace(r"'", "", regex=True)
    df_final = explode_str(df_final, 'ean', ',')
    df_final['ean'] = df_final['ean'].str.strip()
    df_final = df_final.drop_duplicates(subset=['ean'])

    print(df_final)
    df_final.to_csv('df_final.csv')



sheet = 'xxx'
web_scraping(sheet)


