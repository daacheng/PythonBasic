# nginx+flask部署
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
