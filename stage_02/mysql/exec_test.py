
import pymysql,re

db = pymysql.connect(host='localhost',port=3306,user='root',password='zzl20001023',database='dict',charset='utf8')
cur = db.cursor()

try:
    with open('../python_network/dict.txt', encoding='utf-8') as f:
        for line in f:
            obj = re.match(r'^([A-Za-z]+)\s+(.*)',line.strip())
            if obj:
                word,remark = obj.groups()
            sql = "insert into words(word,remark) values(%s,%s)"
            cur.execute(sql,[word,remark])
    db.commit()
except Exception as e:
    db.rollback()
    print(e)
finally:
    cur.close()
    db.close()
