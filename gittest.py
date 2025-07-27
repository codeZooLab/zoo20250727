
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',port=3306,user='root',password='zzl20001023',database='stu',charset='utf8')

# 创建游标 (操作数据库语句,获取查询结果)
cur = db.cursor()

"""
gittest.py
pymysql数据库操作流程演示
"""
# # 数据库操作
# sql = "insert into class values(7,'test',20,'m',60.5) "
# cur.execute(sql)
#
# # 向数据库提交 (可以多次execute一次提交,只有写操作需要)
# db.commit()


"""
read_db.py
数据库读操作示例  select
"""
# # 数据库读操作
# sql="select * from class;"
# cur.execute(sql)
#
# # 获取查询结果
# one_row = cur.fetchone()
# print(one_row) # 元组
#
# many_row = cur.fetchmany(2)
# print(many_row) # 元组套元组
#
# all_row = cur.fetchall()
# print(all_row) # 元组套元组


"""
write_db.py
数据库写操作实例 (insert update delete)
"""
# 数据库操作
try:
    # name = input("name:")
    # age = input("age:")
    # score = input("score:")

    # # 直接构建sql语句
    # sql = "insert into class(name,age,score) values ('%s','%s','%s')"%(name,age,score)
    # cur.execute(sql)

    # # 通过execute第二个参数列表构建sql语句
    # sql = "insert into class(name,age,score) values (%s,%s,%s)"
    # cur.execute(sql,[name, age, score])

    # # 修改操作
    # sql = "update class set age=10 where id = 7 "
    # cur.execute(sql)

    # # 删除操作
    # sql = "delete from class where id = 12"
    # cur.execute(sql)

    # # 存储图片(二进制)
    # with open('../concurrent/network/123.jpeg','rb') as f:
    #     data = f.read()
    # sql = "update class set image = %s where id = 9 "
    # cur.execute(sql,[data])

    # # 提取图片
    # sql = "select image from class where id = 9"
    # cur.execute(sql)
    # data = cur.fetchone()
    # with open('test.jpeg','wb') as f:
    #     f.write(data[0])

    db.commit()
except Exception as e:
    # 如果提交异常则回到提交前的状态
    db.rollback()
    print(e)

# 关闭游标和数据库
cur.close()
db.close()
这是dev创建的分支
呜呼呼
woooo
