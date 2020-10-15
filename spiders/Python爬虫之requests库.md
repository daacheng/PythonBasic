## 一.发送请求
requests提供了http的所有基本请求方式：
```python
import requests
r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")
```

基本get请求中参数的传递：

```python
# requests允许使用params关键字参数，以字典的形式来提供get请求url中的参数。
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)  # http://httpbin.org/get?key2=value2&key1=value1

# 字典中的value还可以以列表的形式传入
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
http://httpbin.org/get?key1=value1&key2=value2&key2=value3
```

添加请求头headers
```python
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
```

Post请求
```python
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
# 可以为 data 参数传入一个元组列表
# 在表单中多个元素使用同一 key 的时候，这种方式尤其有效：
payload = (('key1', 'value1'), ('key1', 'value2'))
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)
{
  ...
  "form": {
    "key1": [
      "value1",
      "value2"
    ]
  },
  ...
}
# post的为json对象
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)
```

超时设置：

```python
requests.get('http://github.com', timeout=0.001)
```

## 二.响应内容
```python
import requests
r = requests.get('https://github.com/timeline.json')
r.encoding='utf-8'
r.text
# [{"repository":{"open_issues":0,"url":"https://github.com/...
```

网页乱码问题:
```python
# 查看网页编码
print(res.apparent_encoding)
# 设置编码
res.encoding = 'GB2312'
```

二进制响应内容(r.content)
```python
from PIL import Image
from io import BytesIO
#BytesIO用于操作内存中的二进制数据
img=Image.open(BytesIO(r.content))
```

JSON响应内容（r.json()）
```python
import requests
r = requests.get('https://github.com/timeline.json')
r.json()
# [{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...
```

响应状态码（r.status_code）
```python
r = requests.get('http://httpbin.org/get')
r.status_code
200
```

响应头(r.headers)
```python
r.headers
{
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json'
}
r.headers['Content-Type']
'application/json'
```

## 三.Cookies
如果某个响应中包含一些 cookie，你可以快速访问它们：
```python
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)

r.cookies['example_cookie_name']
# 'example_cookie_value'
```

要想发送你的cookies到服务器，可以使用 cookies 参数：
```python
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
r.text
# '{"cookies": {"cookies_are": "working"}}'
```

## 四.会话
requests.Session()这样可以在会话中保留状态，保持cookie等
```python
import requests
s = requests.Session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)
```

## 五.代理
如果需要使用代理，你可以通过为任意请求方法提供 proxies 参数来配置单个请求
```python
# http代理
import requests
proxies = {
  "https": "http://41.118.132.69:4433"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
# socks代理
proxies = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port'
}
```
## 六.Prepared Request
构造requests.Request对象，将Request对象作为参数传入requests.Session()对象的prepare_request()方法中，最后通过Session对象的send()方法发送请求。
```python
import requests
from requests import Request
url = 'http://httpbin.org/get'
# 创建Session对象
s = requests.Session()
# 构造Request对象
req = Request('GET',url)
# 将Request对象转换成 PreparedRequest对象
prepped = s.prepare_request(req)
# 利用Session对象的send()方法，发送PreparedRequest对象
res = s.send(prepped)
print(res.text)
print(type(prepped))
```
