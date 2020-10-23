# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

StockName = ""

urlBasic1 = "https://search.daum.net/search?nil_suggest=sugsch&w=news&"
urlBasic2 = "DA=GIQ&sq=&o=1&sugo=30&cluster=y&q="
urlStockName = "삼성전자"
req = requests.get(urlBasic1+urlBasic2+urlStockName)
soup = BeautifulSoup(req.text, 'html.parser')
for anchor in soup.select("div.coll_cont"):
    print(anchor.get.text())
