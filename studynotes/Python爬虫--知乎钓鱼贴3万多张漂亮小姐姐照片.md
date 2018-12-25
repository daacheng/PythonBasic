# Python爬虫--知乎钓鱼贴3万多张漂亮小姐姐照片
## 写在前面
之前爬取了微博指定用户的主页下所有微博图片后  [微博主页图片爬虫](https://github.com/daacheng/PythonBasic/blob/master/studynotes/Python%E7%88%AC%E8%99%AB--%E7%88%AC%E5%8F%96%E5%BE%AE%E5%8D%9A%E6%8C%87%E5%AE%9A%E7%94%A8%E6%88%B7%E4%B8%BB%E9%A1%B5%E4%B8%8B%E7%9A%84%E6%89%80%E6%9C%89%E5%9B%BE%E7%89%87.md)，
就一直在想爬取知乎上漂亮小姐姐的图片，后来研究了一下，发现爬取知乎问题下的答案，其实也不需要模拟登陆，只需要用登陆后的cookie就可以获取到问题下所有的答案了，
返回的数据都是json格式的，也比较简单。目前做的效果是获取某一问题下所有答案中的图片url路径，然后保存成csv文件，最后读取csv文件，开启十个线程去下载图片，
3万多张图片35分钟就下载完了。这里还是用到了之前的代理池系统  [爬虫代理池实现](https://github.com/daacheng/PythonBasic/blob/master/studynotes/Python%E7%88%AC%E8%99%AB--%E4%BB%A3%E7%90%86%E6%B1%A0%E7%BB%B4%E6%8A%A4.md)
虽然知乎好像也没有封IP的说法，但是还是害怕用同一个IP去下载3万多张图片访问太频繁，所以这里还是用了代理池。

代码还有很多可以优化的地方，比如用redis去缓存抓取到的图片url，我这里是用生成csv文件的方式，比较偷懒就没用redis，后面再好好优化一下。

## 大概思路
### 一、请求URL分析
**爬取知乎钓鱼贴，首先要确定哪些是你要爬取的钓鱼贴，比如知乎每一个问题，都有一个对应的id，这里我就去找了下面这20多个帖子，如图：**
![](https://github.com/daacheng/PythonBasic/blob/master/pic/zhihu1.png)
![](https://github.com/daacheng/PythonBasic/blob/master/pic/zhihu2.png)
**随便打开一个帖子，F12打开，不断向下滑动，观察得到一下结果。**
![](https://github.com/daacheng/PythonBasic/blob/master/pic/zhihu3.png)
![](https://github.com/daacheng/PythonBasic/blob/master/pic/zhihu4.png)
**多向下滑动，获取不同的请求url，对比发现URL有什么不同**
![](https://github.com/daacheng/PythonBasic/blob/master/pic/zhihu5.png)

### 二、解析获取图片url
**我们发现了请求url的规律，知道如何获取答案数据，之后就是从答案中解析获取图片url的路径，这个就比较简单了，直接通过正则表达式，就可以获取答案中所有的
图片链接了。**

    r"""<img\s.*?\s?data-original\s*=\s*['|"]?([^\s'"]+).*?>"""

### 三、将获取到的图片url保存到csv文件中
### 四、读取csv文件中的url链接到队列中，开启多线程处理队列取下载图片
### 五、最终结果
![](https://github.com/daacheng/PythonBasic/blob/master/pic/zhihu6.png)
![](https://github.com/daacheng/PythonBasic/blob/master/pic/zhihu7.png)
### 具体代码地址
[知乎钓鱼贴3万多张漂亮小姐姐照片](https://github.com/daacheng/PythonBasic/tree/master/spider/zhihu_spider)
