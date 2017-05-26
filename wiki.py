#! /usr/bin/env python
# encoding:UTF-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
soup = BeautifulSoup(resp, "html.parser")
listUrls = soup.findAll("a", href=re.compile("^/wiki/"))
print(listUrls)
for url in listUrls:
    if not re.search("\.jpg|JPG$", url["href"]):
        print(url.get_text(), "\t\t", url["href"])
