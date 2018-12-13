from lxml import etree

text = """
<div>
<ul>
<li class = "item-0"><a href = "link1.html">first item</a></li>
<li class = "item-1"><a href = "link2.html">second item</a></li>
<li class = "item-inactive"><a href = "link3.html">third item</a></li>
<li class = "item-1"><a href = "link4.html">fourth item</a></li>
<li class = "item-0"><a href = "link5.html">fifth item</a>
</ul>
</div>
"""

# 调用etree的HTML类，使用上面的html初始化html,得到了一个XPath解析对象.
html = etree.HTML(text)

# 注意上面第10行的li是没有闭合的，但是etree模块可以自动修正HTML文本
result = etree.tostring(html)
print(result.decode('utf-8'))