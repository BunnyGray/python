#! /usr/bin/env python
# encoding:UTF-8
import pymysql
# data = ['asd', 'asdqwe', 'asdasdqwe', 'asds', 'asdqwe', 'zxc']
# data = [1, 2, 3, 4, 5, 6]
# data = ["qwe", "qqq", "ccc", "ddd", "eee", "fff"]
data = ['aaa', 'bbb', 'ccc', 'aaa', 'bbb', 'ccc']
# data = ["'qwe'", "'qqq'", "'ccc'", "'ddd'", "'eee'", "'fff'"]
b = ['ftp://6:6@d3.dl1234.com:6689/生化危机4战神再生BD中英双字[电影天堂www.dy2018.com].mp4',
 ['经典美国恐怖科幻片《生化危机4：战神再生》BD中英双字'],
 'ftp://d:d@d3.dl1234.com:3468/硬汉2奉陪到底HD国语中字[电影天堂www.dy2018.com].mkv',
 ['经典刘烨张梓琳爱情动作片《硬汉2：奉陪到底》HD国语中字'],
 'ftp://s:s@d3.dl1234.com:8006/暮光之城3月食BD国英双语双字[电影天堂www.dy2018.com].mkv',
 ['经典美国奇幻爱情片《暮光之城3：月食》BD国英双语双字']]
c = "'aaa'"
# c = 111
a = 1
db = pymysql.connect("127.0.0.1", "root", "", "moviesdata", charset="utf8")
cursor = db.cursor()
for x in range(0, len(data), 2):
    a += 1
    sql = "insert into moviesdata.links(id,name,Thunderlinks)values(%d,'%s','%s')" % \
          (a, data[x], data[x+1])
    try:
        cursor.execute(sql)
        # cursor.execute("insert into links(id,name,Thunderlinks)values(%d,%s,%s)", (a, c, c))
        db.commit()
    except Exception as e:
        db.rollback()
        print("error",e)
db.close()
