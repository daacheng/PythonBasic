## 《图解HTTP》——请求首部
### 一、4种HTTP首部字段类型
**通用首部字段**：请求报文和响应报文两方都会使用的首部</br>
**请求首部字段**：从客户端向服务器端发送请求报文时使用的首部。补充了请求的附加内容、客户端信息、相应内容相关优先级等信息。</br>
**响应首部字段**：从服务器端向客户端返回响应报文时使用的首部。补充了响应的附加内容、也会要求客户端附加额外的内容信息。</br>
**实体首部字段**：针对请求报文和响应报文的实体部分使用的首部。补充了资源内容更新时间等与实体有关的信息。</br>
### 二、通用首部字段
#### 2.1、Cache-Control
**Cache-control**:能够控制缓存的行为。Cache-Control的指令参数是可选的，多个指令通过“，”区分。</br>
Cache-Control:public  表示其他用户也可以利用缓存。</br>
Cache-Control:private  缓存服务器会对该特定用户提供资源缓存的服务，对于其他用户发送过来的请求，代理服务器则不会返回缓存。</br>
Cache-Control:no-cache   **客户端**发送的请求中如果包含 no-cache 指令，则表示客户端将不会接收缓存过的响应（**不要缓存的内容**）。于是，“中间”的缓存服务器必须把客户端请求转发
给源服务器。</br>
**如果服务器**返回的响应中包含 no-cache 指令，那么缓存服务器不能对资源进行缓存。源服务器以后也将不再对缓存服务器请求中提出的资源有效性进行确认，且禁止其对响应资源进行缓存操作。  

Cache-Control: no-store   该指令规定缓存不能在本地存储请求或响应的任一部分。</br>
Cache-Control: max-age=604800（单位：秒）   如果判定缓存资源的缓存时间数值比指定时间的数值更小，那么客户端就接收缓存的资源。</br>
Cache-Control: max-stale=3600（单位：秒）   使用 max-stale 可指示缓存资源，即使过期也照常接收(只要过期时间不超过3600s)。
#### 2.2、Connection
Connection具有两个作用：控制不再转发给代理的首部字段；管理持久连接。</br>
**Connection: 不再转发的首部字段名**   在客户端发送请求和服务器返回响应内，使用 Connection 首部字段，可控制不再转发给代理的首部字段。
**Connection: close**  HTTP/1.1版本的默认连接都是持久连接。为此，客户端会在持久连接上连续发送请求。当服务器端想明确断开连接时，则指定
Connection 首部字段的值为 Close。
#### 2.3、Data
Data首部：表明创建http报文的日期和时间。
#### 2.4、Trailer
**Trailer首字段** 会事先说明在报文主体后记录了哪些首部字段。该首部字段可应用在 HTTP/1.1 版本分块传输编码时。
#### 2.5、Transfer-Encoding
**Transfer-Encoding: chunked** 规定了传输报文主体时采用的编码方式。最新的HTTP规范里，只定义了一种编码传输：分块编码
#### 2.6、Via
Via首部字段是为了追踪客户端与服务器之间的请求和响应报文的传输路径。报文经过代理或网关时，会先在首部字段 Via 中附加该服务器的信息，然后再进行转发。
### 三、请求首部字段
#### 3.1、Accept
Accept通知服务器，用户代理能够处理的媒体类型及媒体类型对应的相对优先级。使用type/subtype的格式。如</br>
Accept:text/html,application/xhtml+xml,image/jpeg
#### 3.2、Accept-Charset
Accept-Charset通知服务器，用户代理支持的字符集及优先级。如  Accept-Charset: iso-8859-5
#### 3.3、Accept-Encoding
**Accept-Encoding: gzip, deflate**：告知服务器用户代理支持的内容编码及内容编码的优先级顺序。
#### 3.4、Accept-Language
**Accept-Language: zh-cn,zh;q=0.7,en-us,en;q=0.3**  用来告知服务器用户代理能够处理的自然语言集（指中文或英文等），及其优先级。
#### 3.5、Authorization
首部字段Authorization是用来告知服务器，用户代理的认证信息（证书值）。
通常，想要通过服务器认证的用户代理会在接收到返回的401状态码响应后，把首部字段Authorization加入请求中。
#### 3.6、From
From 用来告知服务器，使用用户代理的用户的电子邮件地址。
#### 3.7、Host
**Host:www.baidu.com** 首部字段Host会告知服务器，请求的资源所处的互联网主机名和端口号。Host首部字段在HTTP/1.1规范内是唯一一个必须被包含在请
求内的首部字段。
#### 3.8、Referer
**Referer: http://www.hackr.jp/index.htm** 查看Referer可以得知请求的URL是从哪个web页面发起的。
#### 3.9、User-Agent
**User-Agent**会将创建请求的浏览器和用户代理名称等信息传达给服务器。
### 四、响应首部字段
#### 4.1、Accept-Ranges
**Accept-Ranges**是用来告知客户端，服务器是否能处理范围请求，以指定获取服务器端某个部分的资源。可指定的字段值有两种，可处理范围请求时指定其为 bytes，反之则指定其为 none。
#### 4.2、Location
**Location: http://www.usagidesign.jp/sample.html** 提供重定向的url
#### 4.3、Retry-After
**Retry-After: 120** 告知客户端应该在多久之后再次发送请求。主要配合状态码 503 Service Unavailable 响应。
#### 4.4、Server
Server告知客户端，当前服务器上安装的 HTTP 服务器应用程序的信息。
### 五、实体首部字段
#### 5.1、Content-Encoding
**Content-Encoding: gzip** Content-Encoding 会告知客户端和服务器，对实体的主体部分选用的内容编码方式。
#### 5.2、Content-Language(实体主体使用的自然语言)
#### 5.3、Content-Length（主体部分的大小）
#### 5.4、Content-Location（给出与报文主体部分相对应的 URI）
#### 5.5、Content-Type
**Content-Type: text/html; charset=UTF-8** 说明了实体主体内对象的媒体类型。
### 六、Cookie相关
#### 6.1、Set-Cookie（响应首部字段）
当服务器准备开始管理客户端的状态时，会事先告知各种信息。</br>
**Set-Cookie字段**包含的属性有NAME=VALUE，expires=DATE，path=PATH，domain=域名，secure，HttpOnly</br>
NAME：设置Cookies的名称。</br>
expires：属性指定浏览器可发送cookie的有效期。</br>
path: Cookie的path属性可用于限制指定Cookie的发送范围的文件目录。</br>
secure: 用于限制Web页面仅在HTTPS安全连接时，才可以发送 Cookie。仅当在 https://www.example.com/（HTTPS）安全连接的情况下才会进行 Cookie 的回收。也就是说，即使域名相同，http://www.example.com/（HTTP）也不会发生 Cookie 回收行为。</br>
HttpOnly:Cookie 的 HttpOnly 属性是 Cookie 的扩展功能，它使 JavaScript 脚本无法获得 Cookie。其主要目的为防止跨站脚本攻击（Cross-sitescripting，XSS）对 Cookie 的信息窃取。
#### 6.2、Cookie（请求首部字段）
首部字段 Cookie 会告知服务器，当客户端想获得 HTTP 状态管理支持时，就会在请求中包含从服务器接收到的 Cookie。接收到多个
Cookie 时，同样可以以多个 Cookie 形式发送。
