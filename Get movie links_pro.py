#! /usr/bin/env python
import re
import pymysql.cursors
from bs4 import BeautifulSoup
from time import sleep
from urllib.request import urlopen
import urllib.request
hrefs = []
data = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
for i in range(160, 162):
    web_list = str("http://www.dytt8.net/html/gndy/dyzz/list_23_"+str(i)+".html")
    print(web_list, end=" , ")
    r = urllib.request.Request(web_list, headers=headers)
    resp = urlopen(r).read().decode('GBK', errors='ignore')
    soup = BeautifulSoup(resp, "html.parser")
    links = soup.find_all(class_="ulink")
    # links = str(links)
    for urls in links:
        urls = str("http://www.dytt8.net/"+urls['href'])
        hrefs.append(urls)
    links = []
print()
print("waitting", end='')
i = 1
un_effect = 0
ftp = ''
error_links = []
for x in hrefs:
    try:
        resp1 = urlopen(x).read().decode('GBK', errors='ignore')
    except urllib.request.HTTPError as e:
        print(e.code)
        print(e.reason)
    soup1 = BeautifulSoup(resp1, "html.parser")
    try:
        ftp = soup1.find(style="WORD-WRAP: break-word").get_text()
    except:
        un_effect += 1
        error_links.append(x)
        continue
    name = soup1.find(color="#07519a").get_text()
    data.append(ftp)
    data.append(name)
    # for w in range(i):
    print('.', end='', flush=True)
    # print(resp1)
    # print(x)
    sleep(0.01)
    i += 1
print()
print(data)
print("此次爬取到", int(len(data)/2), "个电影资源")
print("打开网页失败", un_effect, "次")
if un_effect != 0:
    print("未打开网页为：", error_links)


# 存入mysql
print("正在存入数据库...")
db = pymysql.connect("127.0.0.1", "root", "", "moviesdata", charset="utf8mb4")
cursor = db.cursor()
sql1 = "select max(id) from links_pro"
cursor.execute(sql1)

# 查询当前表最后一条记录
try:
    db.commit()
    b = cursor.fetchone()[0]
    if b == None:
        b = 0
    # print(b)
except Exception as e:
    db.rollback()
    print("查询最后一条记录失败", e)

# 插入数据库
for i in range(0, len(data), 2):
    db = pymysql.connect("127.0.0.1", "root", "", "moviesdata", charset="utf8mb4")
    cursor = db.cursor()
    b = b+1
    # print("for 内", b)
    sql = "insert into links_pro(id,name,Thunderlinks)values(%d,'%s','%s')" % \
          (b, data[i+1], data[i])
    try:
        cursor.execute(sql)
        db.commit()
        # print(data[i + 1])
    except Exception as e:
        db.rollback()
        print("error", e)

# 删除重复数据
sql_del = """
DROP TABLE IF EXISTS `temp`;
DROP TABLE IF EXISTS `temp2`;
CREATE TABLE `temp`(
	`id` INT(11) NOT NULL,
	`name` VARCHAR(1000)DEFAULT NULL,
	`Thunderlinks` VARCHAR(1000)DEFAULT NULL,
	PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `temp2`(
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(1000)DEFAULT NULL,
	`Thunderlinks` VARCHAR(1000)DEFAULT NULL,
	PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
INSERT into `temp`(
select * from links_pro where Thunderlinks in (select  Thunderlinks from links_pro  group  by  Thunderlinks   having  count(Thunderlinks) > 0)
and id not in (select min(id) from  links_pro  group by Thunderlinks  having count(Thunderlinks)>0));
delete a.* from links_pro a, temp b where a.id = b.id ;
insert into `temp2`(name, Thunderlinks)
(select name, Thunderlinks from links_pro);
DROP TABLE IF EXISTS `links_pro`;
DROP TABLE IF EXISTS `temp`;
alter table temp2 rename links_pro;
"""
try:
    print("正在查询有无重复数据...")
    cursor.execute(sql_del)
    db.commit()
    print('删除重复数据成功')
except Exception as e:
    db.rollback()
    print("删除重复数据失败", e)
db.close()

