# nginx+flask+gunicorn部署
## 写在前面
前段时间爬取了一些漂亮小姐姐的图片，微博，知乎等有差不多20G，于是想着用flask做一个图片网站，方便自己观赏小姐姐，对web开发并不是很熟悉，所以只弄个非常简单的网站，如果有朋友有做图片网站相关经验，可以互相交流，我也想学习学习，我这前端div布局啥的都不熟，网上东拼西凑的，凑合着出了个网站，然后用nginx+guricorn+flask的方式部署。
## 一、正向代理与反向代理
正向代理中客户端非常明确自己要访问的服务器地址，服务器只知道代理来自哪个代理，不知道具体来自哪个客户端。<br>
反向代理，客户端无法感知代理的存在，访问者并不知道自己访问的是代理服务器。
![](https://github.com/daacheng/PythonBasic/blob/master/pic/nginxproxy1.png)
## 二、centos下安装nginx
参考教程 http://www.cnblogs.com/taiyonghai/p/6728707.html
### 2.1. 准备好相关组件

    cd /usr/local/src
    wget http://nginx.org/download/nginx-1.10.2.tar.gz
    wget http://www.openssl.org/source/openssl-fips-2.0.10.tar.gz
    wget http://zlib.net/zlib-1.2.11.tar.gz
    wget ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.40.tar.gz
### 2.2. 安装c++编译环境

    yum install gcc-c++
### 2.3. 安装Nginx及相关组件
#### openssl安装

    tar zxvf openssl-fips-2.0.10.tar.gz
    cd openssl-fips-2.0.10
    ./config && make && make install
#### pcre安装

    tar zxvf pcre-8.40.tar.gz
    cd pcre-8.40
    ./configure && make && make install
#### zlib安装

    tar zxvf zlib-1.2.11.tar.gz
    cd zlib-1.2.11
    ./configure && make && make install
#### nginx安装

    tar zxvf nginx-1.10.2.tar.gz
    cd nginx-1.10.2
    ./configure && make && make install
### 2.4. 启动nginx
* 查看whereis nginx
* cd /usr/local/nginx/sbin
* ./nginx
![](https://github.com/daacheng/PythonBasic/blob/master/pic/nginxproxy2.png)
## 三、nginx基本操作
* 启动： /usr/local/nginx/sbin/nginx
* 停止/重启： /usr/local/nginx/sbin/nginx -s stop(quit、reload)
* 帮助： /usr/local/nginx/sbin/nginx -h
* 配置文件： vim /usr/local/nginx/conf/nginx.conf
## 四、配置nginx
* 修改nginx配置文件 vim /usr/local/nginx/conf/nginx.conf.default
![](https://github.com/daacheng/PythonBasic/blob/master/pic/nginxproxy4.png)
* 重启nginx sbin/nginx -s reload
## 五、安装gunicorn
* pip3 install gunicorn
* 编写run_gunicorn.py

        import re
        import sys
        from gunicorn.app.wsgiapp import run
        if __name__ == '__main__':
            sys.argv[0] = re.sub(r'(-script/.pyw|/.exe)?$', '', sys.argv[0])
            sys.exit(run())
* 在项目根目录运行 nohup python3 run_gunicorn.py -w 4 -b 0.0.0.0:5000 app:app &
* 第一个app是flask服务脚本的名字，我这里是app.py,所以用app，第二个app是app.py中Flask()实例对象的名字，我给取的是app，所以这里是app:app.
## 五、部署成功
![](https://github.com/daacheng/PythonBasic/blob/master/pic/nginxproxy5.png)
