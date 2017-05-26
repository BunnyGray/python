import pymysql.cursors
connection = pymysql.connect(host='localhost',
                                 user ='root',
                                 db ='wikiurl',
                                 charset ='utf8mb4')
try:
    with connection.cursor()as cursor:
        sql = "select urlname`, `urlhref` from `urls`where `id` is not null"
        count = cursor.execute(sql)
        print(count)
finally:
    connection.close()