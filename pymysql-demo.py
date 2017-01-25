import pymysql  # 支持py3

conn = pymysql.connect(host='192.168.104.83', port=3306, user='root', passwd='root',
                       db='database', charset='utf8')

cur = conn.cursor()

sql = 'select * from test'  # replace your sql

cur.execute(sql)

rows = cur.fetchall()

for row in rows:
    print(row)
