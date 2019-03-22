## 一、发送请求
首先导入requests库
<pre><code>import requests</code></pre>
requests提供了http的所有基本请求方式：
<pre><code>r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")</code></pre>
### 基本get请求中参数的传递
requests允许使用<strong>params</strong>关键字参数，以字典的形式来提供get请求url中的参数。
<pre><code>payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)       http://httpbin.org/get?key2=value2&key1=value1
</code></pre>
字典中的value还可以以列表的形式传入
<pre><code>payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
http://httpbin.org/get?key1=value1&key2=value2&key2=value3</code></pre>
## 二、响应内容(r.text)
<pre><code>import requests
r = requests.get('https://github.com/timeline.json')
r.encoding='utf-8'
r.text
u'[{"repository":{"open_issues":0,"url":"https://github.com/...</code></pre>

### 网页乱码问题

    # 查看网页编码
    print(res.apparent_encoding)
    # 设置编码
    res.encoding = 'GB2312'

### 二进制响应内容(r.content)
可以通过字节<strong>r.content</strong>的方式访问请求响应体，对于非文本（比如图片）请求：
<pre><code>
    from PIL import Image
    from io import BytesIO
    #BytesIO用于操作内存中的二进制数据
    img=Image.open(BytesIO(r.content))
</code></pre>
### JSON响应内容（r.json()）
<pre><code>import requests

r = requests.get('https://github.com/timeline.json')
r.json()
[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...</code></pre>
### 响应状态码（r.status_code）
<pre><code>r = requests.get('http://httpbin.org/get')
r.status_code
200</code></pre>
### 响应头(r.headers)
<pre><code>r.headers
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
'application/json'</code></pre>


## 三、添加请求头headers
为请求添加HTTP头部，只需要传递一个dict给参数headers就可以了。
<pre><code>url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)</code></pre>
## 四、POST请求
POST请求传递参数时，只需要传递一个dict给data参数。
<pre><code>payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
{
  ...
  "form": {
    "key2": "value2",
    "key1": "value1"
  },
  ...
}</code></pre>
你还可以为 data 参数传入一个元组列表。在表单中多个元素使用同一 key 的时候，这种方式尤其有效：
<pre><code>payload = (('key1', 'value1'), ('key1', 'value2'))
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
}</code></pre>

也可以为data参数传递一个json对象。
有时候我们需要传送的信息不是表单形式的，需要我们传JSON格式的数据过去，所以我们可以用 json.dumps() 方法把表单数据序列化。
<pre><code>
import json
import requests
 
url = 'http://httpbin.org/post'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print r.text</code></pre>
或者直接传递dict给json参数，他可以自行编码。
<pre><code>url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, json=payload)</code></pre>
## 五、cookies
如果某个响应中包含一些 cookie，你可以快速访问它们：
<pre><code>url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)

r.cookies['example_cookie_name']
'example_cookie_value'</code></pre>
要想发送你的cookies到服务器，可以使用 cookies 参数：
<pre><code>url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
r.text
'{"cookies": {"cookies_are": "working"}}'</code></pre>
## 六、超时设置
<pre><code>requests.get('http://github.com', timeout=0.001)</code></pre>
## 七、会话
requests.Session()这样可以在会话中保留状态，保持cookie等
<pre><code>import requests
 
s = requests.Session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print r.text</code></pre>
## 八、代理（proxies参数）
如果需要使用代理，你可以通过为任意请求方法提供 proxies 参数来配置单个请求
<pre><code>import requests
 
proxies = {
  "https": "http://41.118.132.69:4433"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)</code></pre>
## 九、Prepared Request
构造requests.Request对象，将Request对象作为参数传入requests.Session()对象的prepare_request()方法中，最后通过Session对象的send()方法发送请求。

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
