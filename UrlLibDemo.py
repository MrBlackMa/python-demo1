# 学习使用urllib.


import urllib.request

response=urllib.request.urlopen('https://www.python.org')
#print(response.read().decode('utf-8'))
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))