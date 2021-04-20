# HTTP概念
## 1.定义
HTTP，HyperText Transfer Protocol，超文本（文本，图片，视频等）传输协议，是基于TCP协议的应用层传输协议。

## 2.HTTP的特性
* 灵活：Http允许传输多种类型的数据对象，传输类型在请求头Content-Type中标记
* 无连接：每次连接只处理一个请求，请求时建立连接，请求后释放连接，尽快将资源释放出来服务其他客户端，但随着网页越来越复杂，里面可能嵌套的很多图片，每次访问图片都需要建立一次TCP连接这样就很低效，后来的Keep-Alive解决这个问题，Keep-Alive 功能使客户端到服务器端的连接持续有效，当出现对服务器的后继请求时，Keep-Alive 功能避免了建立或者重新建立连接。
* 无状态：HTTP协议不记录客户端的状态，客户端的每次请求对服务端来说都是独立的。

## 3.URL与URI
* URI:Uniform Resource Identifier,统一资源标识符
* URL:Uniform Resource Locator,统一资源定位符，一段字符串标识资源的定位地址（协议名称+服务器IP+服务器端口+服务器上路径）
* URN:Uniform Resource Name，统一资源名称

**URI重点是对资源的唯一标识，可以通过地址标识资源(URL),也可以通过唯一名称标识资源(URN).**
