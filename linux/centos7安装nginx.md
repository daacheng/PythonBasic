# centos7安装nginx
[参考Nginx安装](https://www.nginx.cn/install)
## 1.centos平台编译环境使用如下指令
```python
# 安装make
yum -y install gcc automake autoconf libtool make
# 安装g++
yum install gcc gcc-c++
```

## 2.开始安装
* 选定源码目录
* 安装PCRE库
* 安装zlib库
* 安装ssl
* 安装nginx

#### 2.1.选定源码目录
```python
# 指定源码的目录
cd /usr/local/src
```
#### 2.2.安装PCRE库
```python
cd /usr/local/src
wget https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.gz
tar -zxvf pcre-8.44.tar.gz
cd pcre-8.44
./configure
make
make install
```
#### 2.3.安装zlib
```python
wget http://zlib.net/zlib-1.2.11.tar.gz
tar -zxvf zlib-1.2.11.tar.gz
cd zlib-1.2.11
./configure
make
make install
```
#### 2.4.安装ssl
```python
wget https://www.openssl.org/source/openssl-1.1.1g.tar.gz
tar -zxvf openssl-1.1.1g.tar.gz
cd openssl-1.1.1g
./config
make
make install
```
#### 2.5.安装nginx
```python
wget http://nginx.org/download/nginx-1.18.0.tar.gz
tar -zxvf nginx-1.18.0.tar.gz
cd nginx-1.18.0

# 默认安装
./configure & make & make install

# 自定义编译安装
# ./configure --sbin-path=/usr/local/nginx/nginx \
# --conf-path=/usr/local/nginx/nginx.conf \
# --pid-path=/usr/local/nginx/nginx.pid \
# --with-http_gzip_static_module \
# --with-http_stub_status_module \
# --with-file-aio \
# --with-http_realip_module \
# --with-http_ssl_module \
# --with-pcre=/usr/local/src/pcre-8.44 \
# --with-zlib=/usr/local/src/zlib-1.2.11 \
# --with-openssl=/usr/local/src/openssl-1.1.1g

# make
# make install
```

**Nginx编译选项**

* --prefix=path： 自定义nginx的安装目录，默认/usr/local/nginx
* --sbin-path=path：定义nginx可执行文件的路径，默认prefix/sbin/nginx
* --conf-path=path：设置nginx.conf配置文件路径，默认prefix/conf/nginx.conf，可以通过nginx -c config_path,启动的时候指定配置文件
* --pid-path=path： 设置nginx.pid文件，将存储的主进程的进程号，默认prefix/logs/nginx.pid
* --error-log-path=path： 设置主错误，警告，和诊断文件的名称，默认prefix/logs/error.log
* --http-log-path=path：  设置主请求的HTTP服务器的日志文件的名称，默认prefix/logs/access.log
* --user=name  设置nginx工作进程的用户，默认nobody
* --group=name  设置nginx工作进程的用户组
* --with-pcre=/usr/local/src/pcre-8.44： 指定pcre源码路径
* --with-zlib=/usr/local/src/zlib-1.2.11: 指定zlib源码路径
* --with-openssl=/usr/local/src/openssl-1.1.1g： 指定ssl源码路径

## 3.运行nginx
```python
[root@iZ8vb6ughzbdqkfd58dowoZ nginx]# ls
client_body_temp  fastcgi.conf.default    fastcgi_temp  koi-win     mime.types.default  nginx.conf.default  sbin                 scgi_temp             uwsgi_temp
conf              fastcgi_params          html          logs        nginx               nginx.pid           scgi_params          uwsgi_params          win-utf
fastcgi.conf      fastcgi_params.default  koi-utf       mime.types  nginx.conf          proxy_temp          scgi_params.default  uwsgi_params.default
[root@iZ8vb6ughzbdqkfd58dowoZ nginx]# ./nginx
```

* 启动： /usr/local/nginx/sbin/nginx
* 停止/重启： /usr/local/nginx/sbin/nginx -s stop(quit、reload)
* 帮助： /usr/local/nginx/sbin/nginx -h
* 配置文件： vim /usr/local/nginx/conf/nginx.conf
