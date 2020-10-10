# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

StockName = ""

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=주식" + StockName
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')
for anchor in soup.select(".txt_sub"):
    text = anchor.get_text()
    print(text[0:6])
