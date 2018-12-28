# Linux常用操作命令
* 查看程序softname的进程id  **:  ps -ef | grep softname**
* 后台运行程序  **:  nohup python3 others2bh.py &** 
* 删除文件夹  **:  rm -rf 目录名字**
* 删除文件  **:  rm 文件名**
* 批量删除文件  **： find . -name "*.java" |xargs rm -rfv**
* 接收文件  **: rz**
* 发送文件  **: sz**
* 复制粘贴文件  **: cp 源文件或目录 目标文件或目录**
* 查看文件的行数  **：wc -l 文件名**
* 按照大小切分文件  **：split -b 100m 文件名**
* 按照行数切分文件  **：split -l 10000 文件名**
* 查看目录下文件大小  **：du -ah --max-depth=1  （a表示显示目录下所有的文件和文件夹（不含子目录），h表示以人类能看懂的方式，max-depth表示目录的深度）**
* 查看当前目录下有多少个文件及文件夹  **：ls | wc -w**
* 查看当前目录下有多少个文件  **：ls | wc -c**
* 查看当前目录下有多少个指定类型的文件(包含子文件夹) **:ls -lR|grep ".jpg"|wc -l** 
* 查看端口状态  **：netstat -ano | grep 10088**
* linux后台运行  **：nohup command > myout.file 2>&1 &**


## linux下离线安装python，先下载压缩包
    mkdir -p /usr/local/python3/
    # rpm -ivh ./package/zlib-devel-1.2.7-17.el7.x86_64.rpm
    tar zxvf Python-3.6.4.tgz
    cd ./Python-3.6.4
    ./configure --prefix=/usr/local/python3
    make && make install
    ln -s /usr/local/python3/bin/python3 /usr/bin/python3
    ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
    cd ..

## linux下安装setuptools

    tar -zxvf setuptools-19.6.tar.gz
    cd setuptools-19.6.tar.gz
    python3 setup.py build
    python3 setup.py install
