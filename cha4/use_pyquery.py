import requests
from pyquery import  PyQuery as pq

html = '''
<div>
<ul>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0" active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''

doc = pq(html)
print(doc('li'))

# URL的初始化
# doc=pq(url='https://cuiqingcai.com')
print(doc('title'))
# 同下
# doc=pq(requests.get('https://cuiqingcai.com').text)
print(doc('title'))

# 文件初始化
#  除了传递URL,还可以传递本地文件名，此时将参数指定为filename即可
doc = pq(filename='test.html')
print(doc('li'))

# 基本CSS选择器
# 首先用一个实例来感受pyquery的CSS选择器的用法
html = '''
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
doc = pq(html)
print("CSS选择器")
print(doc('#container .list li'))
print(type(doc('#container .list li')))

# 查找节点
# 子节点
print("查找子节点")
items = doc('.list')
print(type(items))
print(items)
print("使用find()方法")
lis = items.find('li')
print(type(lis))
print(lis)

# find()查找范围是节点的所有子孙节点，若只找子节点，可以使用children()方法
print("使用children方法")
list = items.children()
print(type(list))
print(lis)

#  父节点
html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html)
items = doc('.list')
container = items.parent()
print("查找父节点")
print(type(container))
print(container)

# 上面只找爹，如果要找比他爹更大一辈儿的，如下
items = doc('.list')
parents = items.parents()
print("找祖先节点")
print(type(parents))
print(parents)

# 筛选某个祖先节点
print("筛选某个祖先节点")
parent = items.parents('.wrap')
print(parent)

# 兄弟节点
doc = pq(html)
print("兄弟节点")
li = doc(' .list .item-0.active')
print(li.siblings())
# 从兄弟节点中筛选
print("从兄弟节点中筛选")
print(li.siblings('.active'))


# 遍历
# 对于单个节点来说，可以直接打印输出，也可以直接转成字符串
li = doc('.item-0.active')
print("遍历")
print(li)
print(str(li))

# 对于多节点的结果，需要遍历获取。如把每一个li节点进行遍历，需要调用items()方法
from pyquery import PyQuery as pq
doc = pq(html)
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li,type(li))

# 获取信息
# 获取属性
html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html)
a = doc('.item-0.active a')
print(a, type(a))
print(a.attr('href'))

a = doc('a')
print(a, type(a))
# 当返回结果包含多个节点时，调用attr()方法，只会得到第一个节点的属性
print(a.attr('href'))
print(a.attr.href)
# 如果遇到这种情况，就需要用到前面的遍历了
a = doc('a')
print("使用前面所说的遍历")
for item in a.items():
    print(item.attr('href'))

# 获取文本
html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html)
a = doc('.item-0.active a')
print(a)
print(a.text())

li = doc('.item-0.active')
print(li)
print(li.html())

# 另一个问题，如果我们选中的结果是多个节点，text()或html()会返回什么内容？
html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-1"><a href="link2.html>second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html)
li = doc('li')
print(li.html())
print(li.text())
print(type(li.text()))


# 节点操作
# 节点操作方法太多，下面举几个典型例子来说明
html='''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)

# attr、text和html
html = '''
<ul class="list">
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
print("使用attr、text和html")
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.attr('name','link')
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)

# remove()
print("使用remove")
html = '''
<div class="wrap">
    Hello,World
<p>This is a paragraph.</p>
</div>
'''
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())

wrap.find('p').remove()
print(wrap.text())

# 伪类选择器
html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
print("伪类选择")
doc = pq(html)
li = doc('li:first-child')
print(li)
li= doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)