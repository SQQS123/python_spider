import urllib.request
import urllib.parse
import urllib.request
import urllib.error
import socket



response = urllib.request.urlopen('http://www.python.org')

# 显示网页内容
# print(response.read().decode('utf-8'))

print(type(response))

print(response.status)
print(response.getheaders())
print(response.getheader('Server'))


data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read())


# use timeout

response = urllib.request.urlopen('http://www.python.org',timeout=1)
# 打印出网页内容
# print(response.read())

try:
	response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
	if isinstance(e.reason,socket.timeout):
		print("TIME OUT")

# 来感受一下request的用法
request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

