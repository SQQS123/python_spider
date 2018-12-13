import re

from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string)

# 基本用法
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;an their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')
print(soup.prettify())
print('\n\r')
print(soup.title.string)

#  选择元素
print('\r\n')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)

# 提取信息
#(1)获取名称
print(soup.title.name)
#(2)获取属性
print('\r\n')
print(soup.p.attrs)
print(soup.p.attrs['name'])
# 上面的看起来很繁琐
print('\r\n')
print(soup.p['name'])
print(soup.p['class'])

#(3)获取内容
print('\r\n')
print(soup.p.string)

# 嵌套选择
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
"""
soup = BeautifulSoup(html,'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)

# 关联选择
html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
    Once upon a time threr were three little sisters;and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.
</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html,'lxml')
print('\r\n')
# 子节点和子孙节点
print(soup.p.contents)

# 我们可以调用children属性得到相应的结果:
print('\r\n')
print(soup.p.children)
print('\n')
for i,child in enumerate(soup.p.children):
    print(i, child)

# 如果要得到所有的子孙节点的话，可以调用descendants属性
print(soup.p.descendants)
for i,child in enumerate(soup.p.descendants):
    print(i,child)

# 父节点和祖先节点
# 如果要获取某个节点元素的父节点，可以调用parent属性:
html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
    Once upon a time there were three little sisters; and their names were
<a href = "http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
</p>
<p class="story">...</p> 
"""
soup = BeautifulSoup(html,'lxml')
print('\r')
# 这里我们选择的是第一个a节点的父节点元素。其父节点是p节点，输出结果是p节点及其内部的内容
print(soup.a.parent)

# 需要注意的是这里只是找了a节点的直接父节点，，没有再向外寻找父节点的祖先节点，如果想获取所有祖先节点，可以使用parents属性
html = """
<html>
<body>
<p class="story">
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
</p>
"""
soup = BeautifulSoup(html,'lxml')
# 返回结果是生成器类型
print(type(soup.a.parents))
print(list(enumerate(soup.a.parents)))

# 兄弟节点
html = """
<html>
<body>
<p class="story">
    Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
        Hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
        and they lived at the bottom of a well.
</p>
"""
soup = BeautifulSoup(html, 'lxml')
print('\r\n')
print('Next Sibling', soup.a.next_sibling)
print('Prev Sibling', soup.a.previous_sibling)
print('Next Siblings', list(enumerate(soup.a.next_siblings)))
print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))


# 提取信息
html = """
<html>
<body>
<p class="story">
        Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
</p>
"""
soup = BeautifulSoup(html,'lxml')
print('\r\n')
print('Next Sibling:\r')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('\r\n')
print('Parent:\r')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])

# 提取信息
html = """
<html>
<body>
<p class="stroy">
        Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
</p>
"""

soup = BeautifulSoup(html, 'lxml')
print('Next Sibling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])

# 方法选择器
# find_all()
# (1) name
html = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''

soup = BeautifulSoup(html,'lxml')
print(soup.find_all(name='ul'))
# 返回的是tag类型，所有依然可以进行嵌套查询
print(type(soup.find_all(name='ul')[0]))

print("嵌套查询")
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    # 可以遍历每个li获取它的文本
    for li in ul.find_all(name='li'):
        print(li.string)

# attrs
# 也可以通过属性来查询
print("通过属性查询")
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))
# 对于一些常用的属性我们可以不用attrs直接传
print("使用id直接传")
print(soup.find_all(id='list-1'))
print("使用class_传递")
print(soup.find_all(class_ = 'element'))

# text
html = '''
<div class="panel">
<div class="panel-body">
<a>Hello, this is a link</a>
<a>Hello, this is a link, too</a>
</div>
</div>
'''
soup = BeautifulSoup(html,'lxml')
print(soup.find_all(text=re.compile('link')))

# find()
# 返回单个元素，即第一个匹配的元素
html = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''

soup = BeautifulSoup(html,'lxml')
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))

# CSS选择器
html = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''
soup = BeautifulSoup(html,'lxml')
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))

# 嵌套选择，样例如下(先选择素有ul节点，再遍历每个ul节点，选择其li节点)
soup = BeautifulSoup(html,'lxml')
for ul in soup.select('ul'):
    print(ul.select('li'))

# 属性获取
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

# 获取文本
for li in soup.select('li'):
    print('Get Text:',li.get_text())
    print('String:',li.string)