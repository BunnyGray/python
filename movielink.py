#! /usr/bin/env python
# encoding:UTF-8
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

html_doc1 = urlopen("http://www.dytt8.net/html/gndy/dyzz/20170327/53562.html").read().decode("gbk")
soup = BeautifulSoup(urlopen("http://www.dytt8.net/html/gndy/dyzz/20170327/53562.html").read().decode("gbk"), "html.parser")
print(html_doc1)
print(soup)
