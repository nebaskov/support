import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup as bs
import threading


def time_error_raiser():
        return RuntimeError


def pars(url):
    headers = {
        'Accept': '*/*',
        'User-agent': """Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"""
    }
    if 'navigator.sk.ru' in url:
        print('skip navigator.sk.ru')
        return 'navigator_error'
    else:
        try:
            timer = threading.Timer(20, time_error_raiser())
            timer.start()
            req = requests.get(url, headers=headers)
            src = req.text
            soup = bs(src, 'lxml')
            timer.cancel()
            href = None
            href = soup.find('a', {'href': '/about'})
            if href is not None:
                timer.start()
                nreq = requests.get(url+'/about', headers=headers)
                nsrc = nreq.text
                timer.cancel()
                text = bs(nsrc, 'lxml').text.replace('\n', ' ')
            else:
                text = soup.text.replace('\n', ' ')
            print(f'{url} was processed.')
            return text
        
        except:
            mistakes.append(url)
            print(f'Processing {url} returned an error.')
            return 'error'

        
data = pd.read_excel('ufo\company_info.xlsx')
empty_info_ser = pd.Series(np.zeros(len(data['global_id'])), index=data.index, name='info_from_site')
data = data.merge(empty_info_ser, right_index=True, left_index=True)
mistakes = []

for idx in data.index:
    sample = data.iloc[idx]
    info_from_site = pars(sample['Сайт'])
    data.loc[idx, 'info_from_site'] = info_from_site

data.to_excel('company_site.xlsx')

with open('error_url.txt', 'w') as file:
    for url in mistakes:
        file.write(url + '\n')