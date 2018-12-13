from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())

# *代表匹配所有的节点
result = html.xpath('//*')
print(result)

# 指定节点名称
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li')
print(result)
print(result[0])

# 子节点
# 我们通过/或//即可查找元素的子节点或子孙节点
html = etree.parse('./test.html', etree.HTMLParser())
# 获取所有li节点的所有直接a子节点
result = html.xpath('//li/a')
print(result)

# 若要获取所有子孙节点，使用//
result = html.xpath('//li//a')
print(result)

# 如果用//ul/a得不到结果，因为ul下没有直接子节点a
result = html.xpath('//ul/a')
print(result)

# 父节点
# 找到href属性为link4.html的a标签的父节点的class属性
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

# 上面也可以这样写,使用parent::
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

# 属性匹配
result = html.xpath('//li[@class="item-0"]')
print(result)

# 文本获取
result = html.xpath('//li[@class="item-0"]/text()')
print(result)
# 出现了问题
#  如果想要获取li节点内部的文本，有两种方式，一种是先选取a节点再获取文本，另一种是使用//。
# 首先选取到a节点再获取文本，代码如下
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)
# 另一种方式，使用//获取结果
result = html.xpath('//li[@class="item-0"]//text()')
print(result)

# 属性获取
result = html.xpath('//li/a/@href')
print(result)

# 属性多值匹配
text = """
<li class="li li-first"><a href="link.html">first item</a></li>
"""
html = etree.HTML(text)
# 由于上面的class有两个值，所以如果像下面这样使用属性匹配就无法匹配了。
result = html.xpath('//li[@class="li"]/a/text()')
print(result)

# 这时需要使用contains()函数。
result = html.xpath('//li[contains(@class,"li")]/a/text()')
print(result)

# 多属性匹配
text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(result)

# 按序选择
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)

# 节点轴选择
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
print('\n')

html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')
print(result)
result = html.xpath('//li[1]/following-sibling::*')
print(result)