import json

str ='''
[{
    "name":"Bob",
    "gender":"male",
    "birthday":"1992-10-18"
},{
    "name":"Selina",
    "gender":"female",
    "birthday":"1995-10-18"
}]
'''
print(type(str))
data = json.loads(str)
print(data)
print(type(data))

# 这里使用loads()方法将字符串转为JSON对象，外层是中括号，所以最终的类型是列表类型
# 使用如下方式
print(data[0]['name'])
print(data[0].get('name'))

print(data[0].get('age'))
print(data[0].get('age',25))


# 值得注意的是，JSON的数据需要用双引号来包围，不能使用单引号。

# 从JSON文本中读取内容
with open('data.json', 'r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)

# 输出JSON
data = [{
    "name":"Bob",
    "gender":"male",
    "birthday":"1992-10-18"
}]
with open('data1.json', 'w') as file:
    file.write(json.dumps(data))

with open('data2.json', 'w') as file:
    file.write(json.dumps(data, indent=2))

data = [{
    "name":"王伟",
    "gender":"男",
    "birthday":"1992-10-18"
}]
with open('data3.json', 'w') as file:
    file.write(json.dumps(data,indent=2))

# 为了输出中文，需要制定参数ensure_ascii为False
with open('data4.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data,indent=2,ensure_ascii=False))
