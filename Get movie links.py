#! /usr/bin/env python
# encoding:UTF-8
import re
import pymysql.cursors
from bs4 import BeautifulSoup
from urllib.request import urlopen
resp = urlopen("http://www.dy2018.com/html/gndy/index.html").read().decode("gbk")
soup = BeautifulSoup(resp, "html.parser")
links = soup.find_all(class_="inddline")
links = str(links)
soup2 = BeautifulSoup(links, "html.parser")
href = soup2.find_all('a')
hrefs = []
data = []
for url in href:
    urls = str("http://www.dy2018.com/"+url['href'])
    if not (urls == 'http://www.dy2018.com//html/gndy/jddyy/'or urls == 'http://www.dy2018.com//html/gndy/dyzz/'or urls =='http://www.dy2018.com//html/gndy/jddy/'):
        hrefs.append(urls)
for x in hrefs:
    resp1 = urlopen(x).read().decode("gbk")
    soup1 = BeautifulSoup(resp1, "html.parser")
    ftp = soup1.find(bgcolor="#fdfddf").get_text()
    text = soup1.find("title").get_text()
    name = re.findall(r"(?<=年|月|《).+(?=迅雷|》)", text)
    data.append(ftp)
    data.append(name[0])
# print(data)
db = pymysql.connect("127.0.0.1", "root", "", "moviesdata", charset="utf8mb4")
cursor = db.cursor()
sql1 = "select max(id) from links"
cursor.execute(sql1)
try:
    db.commit()
    b = cursor.fetchone()[0]
    if b == None:
        b = 0
    # print(b)
except Exception as e:
    db.rollback()
    print("查询最后一条记录失败", e)
for i in range(0, len(data), 2):
    db = pymysql.connect("127.0.0.1", "root", "", "moviesdata", charset="utf8mb4")
    cursor = db.cursor()
    b = b+1
    # print("for 内", b)
    sql = "insert into links(id,name,Thunderlinks)values(%d,'%s','%s')" % \
          (b, data[i+1], data[i])
    try:
        cursor.execute(sql)
        db.commit()
        # print(data[i + 1])
    except Exception as e:
        db.rollback()
        print("error", e)
sql_del = """
DELETE FROM links WHERE id in(select * from (select MAX(id) from links group by Thunderlinks having count(Thunderlinks) > 1) as b)
"""
try:
    cursor.execute(sql_del)
    db.commit()
except Exception as e:
    db.rollback()
    print("删除重复数据失败", e)
db.close()


