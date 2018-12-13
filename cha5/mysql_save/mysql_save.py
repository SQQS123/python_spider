import pymysql

# db = pymysql.connect(host='localhost',user='root',password='123456',port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:',data)
# # cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()

# 上面我们创建了一个数据库
# db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS student (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY  KEY (id))'
# cursor.execute(sql)
# db.close()

# 上面我们创建了一个名为students的数据表


# 插入数据

id = '20120001'

user = 'Bob'
age = 20

db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
cursor = db.cursor()
# sql = 'INSERT INTO student(id,name,age) values(%s,%s,%s)'
# # 下面是数据库事务的写法
# try:
#     cursor.execute(sql,(id,user,age))
#     db.commit()
# except:
#     print("未成功")
#     db.rollback()
# db.close()

# 事务的改良写法，使用一个字典, 抛出了一个异常


# data = {
#     'id':'20120002',
#     'name':'Bob2',
#     'age':22
# }
# table='student'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
# try:
#     if cursor.execute(sql, tuple(data.values())):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()


# 更新数据
sql = 'UPDATE student SET age = %s WHERE name = %s'
try:
    cursor.execute(sql, (18,'Bob'))
    db.commit()
except:
    db.rollback()
db.close()

# 上面把数据库关了，所以下面还得重新打开一下数据库。。。

# 这种做法支持灵活 的字典传值
db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
cursor = db.cursor()

data = {
    'id':'20120001',
    'name':'Bob',
    'age':21
}

table = 'student'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table,keys=keys,values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print("成功")
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()


# 删除数据
db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
cursor = db.cursor()

table = 'student'
condition = 'age > 20'

sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    print("失败")
    db.rollback()
db.close()



# 查询数据
db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='spiders')
cursor = db.cursor()
sql = 'SELECT * FROM student WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    one = cursor.fetchone()
    print('One:',one)
    results = cursor.fetchall()
    print('Results:',results)
    print('Results Type:',type(results))
    for row in results:
        print(row)
except:
    print('Error')