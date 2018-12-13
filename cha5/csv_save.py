import  csv

# 写入
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerow(['10001','Mike',20])
    writer.writerow(['10002','Bob',22])
    writer.writerow(['10003','Jordan',21])


# 如果想修改列与列之间的分隔符，可以传入delimiter参数，代码如下
with open('data1.csv','w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001','Mike',20])
    writer.writerow(['10002','Bob',22])
    writer.writerow(['10003','Jordan',21])

# 另外，我们也可以调用writerows()方法同时写入多行，此时参数就需要为二维列表
with open('data2.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerow([['10001','Mike',20],['10002','Bob',22],['10003','Jordan',21]])

# 但是一般情况下，爬虫爬取的都是结构化数据，我们一般会用字典来表示。在csv库中也提供了字典的写入方式
with open('data3.csv','w') as csvfile:
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'10001','name':'Mike','age':20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

 # 追加数据
with open('data3.csv','a') as csvfile:
     fieldnames = ['id','name','age']
     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
     writer.writerow({'id':'10004','name':'Durant','age':22})


# 字符编码问题
with open('data3.csv','a',encoding='utf-8') as csvfile:
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writerow({'id':'10005','name':'王伟','age':22})


# 读取
with open('data3.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

#  还可以利用pandas中的read_csv()方法将数据从CSV中读取出来
import pandas as pd

df = pd.read_csv('data3.csv')
print(df)