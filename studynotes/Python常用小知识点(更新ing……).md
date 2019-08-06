## 1.时间转换成指定格式
#### time
    import time
    time.time()                        # 1529653382.830719
    
    # time.struct_time(tm_year=2018, tm_mon=5, tm_mday=16, tm_hour=10, tm_min=21, tm_sec=2, tm_wday=2, tm_yday=136, tm_isdst=0) 
    time.localtime()                
       
    # 把时间（time.struct_time）转换成指定格式的字符串
    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())       # '2018-06-22 15:49:59'
    
    # 把时间戳转换为指定格式字符串
    time.strftime('%Y%m%d%H%M%S', time.localtime(1529653382.830719))
#### datetime

    import datetime

    #  把 “指定格式的时间字符串”  转换为“datetime对象”
    dt_str = '2018-02-09 07:19:50'
    dt_obj = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")   
    dt_obj                                       #  datetime.datetime(2018, 2, 9, 7, 19, 50)


    # 把“datetime对象”  转换为   “指定格式的时间字符串”
    dt_obj.strftime("%Y%m%d%H%M%S")                #  '20180209071950'


    # 把“指定格式的时间字符串” 转换为  “时间戳对象”
    dt_obj = datetime.datetime.strptime(s , "%Y-%m-%d %H:%M:%S")  
    time.mktime(dt_obj.timetuple())                                                    # 1518131990.0
 
    # 把“指定格式的时间字符串” 转换为  “时间戳对象”
    time.mktime(time.strptime(s,'%Y-%m-%d %H:%M:%S'))              # 1518131990.0

## 2.十六进制字符串转字节串

    data = '7c900030000001780000000030303035'
    bytes().fromhex(data)
    b'|\x90\x000\x00\x00\x01x\x00\x00\x00\x000005'
    
## 字节转十六进制字符串

    def bytes_to_hex_str(bytes_data):
        if bytes_data:
            return ''.join(['%02x' % b for b in bytes_data])
        else:
            return ''
## 字节转换成十六进制字节

    hex(ord(b'K'))  # 0x4b     K是ascii中可见字符，所以编辑器在碰到0x4b的时候就把0x4b转换成了b'K'

## 字节转换成十六进制表示

    import binascii
    data = b'\\\x00?\x00?\x00\\\x00E\x00:\x00'
    print(binascii.hexlify(data))  # b'5c003f003f005c0045003a00'

## 3.struct用法

    unpack反序列化:字节转换成常用数据类型

      data = '7c90000B00001818000000003235303630303035'
      import struct
      struct.unpack('>H', bytes.fromhex(data)[2:4])[0]==0x0B      #True

    pack序列化:常用数据类型转换成字节

      s = struct.Struct('III')
      s.pack(12,15,16)    #b'\x0c\x00\x00\x00\x0f\x00\x00\x00\x10\x00\x00\x00'

## 4.写while 死循环，一定要sleep，无论中间代码耗时多少，必须sleep。
## 5. os模块相关

    os.sep  表示 '\\'反斜杠
     r''里面的内容表示不转义，使用真实字符串
    filepath = r'C:\Users\daacheng\Desktop\bl_dev\imsiimei_whcs_bh_yyzkdw_dzwl_20180510103417_120.bcp'
    file_name = os.path.split(filepath)[1]     #文件名  imsiimei_whcs_bh_yyzkdw_dzwl_20180510103417_120.bcp
    file_ext = os.path.splitext(filepath)[1]   #文件后缀 .bcp
    # 文件或文件夹重命名
    os.rename(src, dst)
    # 查看文件大小
    os.path.getsize(file_path)
    # 运行操作系统cmd命令(从一个命令打开一个管道),例如：
    os.popen('jupyter notebook')
    pr = os.popen('wc -l test.txt')
    # 可以查看返回的执行结果   15 test.py
    pr.read() 
    # 获取文件的最后修改时间
    os.stat(file_path).st_mtime

## 6.创建临时文件

    import tempfile
    import os
    tmpfd, tmp_file_path = tempfile.mkstemp()
    print(tmpfd)   #文件描述符
    print(tmp_file_path)   #临时文件的绝对路径
    os.close(tmpfd)   #关闭文件

    # 防止占用资源
    tempfile.mktemp()  #mktemp用于返回一个临时文件的路径，但并不创建该临时文件。

## 7.生成xml文件

    import xml.dom.minidom as Dom 
    # 创建XML文档
    doc = Dom.Document()
    # 创建根节点
    root = doc.createElement('html')
    # 创建h1节点
    h1 = doc.createElement('h1')
    h1.setAttribute('name','aaaa')
    h1.setAttribute('value','hhhhh')

    h1.appendChild(doc.createTextNode('hello world'))

    doc.appendChild(root)
    # 把h1节点作为root的子节点进行添加
    root.appendChild(h1)

    f = open("test2.xml", "w",encoding='utf-8')  
    doc.writexml(f, addindent='\t', newl='\n', encoding="utf-8") 
    f.close()  
    
    <?xml version="1.0" encoding="utf-8"?>
    <html>
        <h1 name="aaaa" value="hhhhh">hello world</h1>
    </html>

## 8.utf8-BOM文件处理
如果文件已utf-8BOM开头，肉眼发现不了，但是对文件转换会造成影响，需要处理

    with open(dev_filepath, 'r+b') as f:
        data = f.read()
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            f.seek(0)
            f.truncate()
            f.write(data)
## 9、Python解析命令行参数--getopt模块

    import getopt
    import sys
    print(sys.argv[1:])  # ['-h', '-t', 'bb', '-i', 'cc']
    opts, args = getopt.getopt(sys.argv[1:], 'i:o:e:c:f:t:h', ['check','output='])
    print(opts)
    print(args)

    # getopt中需要三个参数
    # 1、使用sys.argv[1:]过滤掉第一个参数（执行的脚本的名字，这个不需要）
    # 2、短格式分析串：'i:o:e:c:fh' 分别代表 -i -o -e -c -f 命令。后面有":"表示需要带参数。
    # 3、长格式分析串列表： ['check','output='] 表示 "help"命令 和 "output"命令，"="表示需要带参数。
    # 函数返回两个列表  opts, args   
    # args为不属于格式信息的剩余的命令行参数,即不是按照getopt()里面定义的长或短选项字符和附加参数以外的信息。
    # 例如： 运行命令     python .\test.py -h  -t bb -i cc
    # opts = [('-h', ''), ('-t', 'bb'), ('-i', 'cc')]
    # args = []

## 10、字符串相关

##### isdigit() 判断字符串是否只有数字组成
    'a456'.isdigit()  # False

##### 字符串平均分
    import re
    '-'.join(re.findall(r'.{2}', 'F0B42998CE34'))  # 'F0-B4-29-98-CE-34'

## 11、print不换行(print('aaa',end=""))
    for i in range(1,10):
        print('')
        for j in range(1,i+1):
            print('%d*%d=%d ' %  (i,j,i*j),end="")
## 12、配置文件读取(configparser)
#### 配置文件格式
    [mysql]
    host = 172.16.2.207
    port = 3306
    db = WWW
    user = EEE
    passwd = 123445

    [csv]
    print_num = 100000
#### configparser库
    import configparser

    # 配置文件由节(sections)、键(key)、值(value)组成

    config = configparser.ConfigParser()
    config.read("all_export_conf", encoding='utf-8')


    # 获取配置文件所有的节sections   ['mysql', 'csv']
    config.sections()

    # 获取某个节中的所有键   ['host', 'port', 'db', 'user', 'passwd']
    config.options('mysql')

    # 获取某个节中的某个键对应的value   '172.16.2.207'
    config.get('mysql','host')
    config.get('mysql','port')

    # 添加一个配置文件节点
    config.add_section('test')

    # 给节点添加键值对
    config.set('test','name','daacheng')
## 13、判断两个字符串的相似度（difflib）
    import difflib

    str1 = '广东省揭东县登岗镇洋滇村东磨区西门楼九号'
    str2 = '广东省揭东甚登岗镇洋滇村东膺区西闫楼九号'
    seq = difflib.SequenceMatcher(None, str1,str2)
    ratio = seq.ratio()
    print('相似度: ', ratio)
## 14、set()集合
#### remove()删除元素，元素不存在会报错
    a=set('abcdefghijk')
    a.remove('a')
    a  # {'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'}
#### discard()删除元素，元素不存在不会报错
    a=set('abcdefghijk')
    a.discard('m')
    a  # {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'}
## 15、divmod()函数

    # 给定两个参数，返回两个参数的“商”和“余数”
    divmod(7,2)  # (3, 1)
    divmod(10,5)  # (2, 0)

## 16、Python中网络字节序（大端）与主机字节序转换

    import socket
    import struct
    x = 1234 
    # socket.ntohl()  把(32bit)正整数从网络序转换成主机字节序
    socket.ntohl(x)   # 3523477504

    # socket.ntohs()   把(16bit)正整数从网络序转换成主机字节序
    socket.ntohs(x) # 53764

    #  socket.htonl(x)  把(32bit)正整数从主机字节序转换成网络序
    socket.htonl(3523477504)      # 1234

    # socket.htons(x)   把(16bit)正整数从主机字节序转换成网络序
    socket.htons(53764)           # 1234

    # 字符串IPv4转换为 长度为4的字节串（32bit）
    socket.inet_aton('192.168.1.11')   # b'\xc0\xa8\x01\x0b'

    # 长度为4的字节串（32bit）转换为 字符串IPv4
    socket.inet_ntoa(b'\xc0\xa8\x01\x0b')    # '192.168.1.11'

    # 把标准字符串形式的IP  转换成  网络字节序(大端) 整型表示的IP
    struct.unpack(">I", socket.inet_aton('192.168.1.11'))[0]   # 3232235787

    # 把网络字节序 整型表示的IP 转换成标准字符串形式的IP
    socket.inet_ntoa(struct.pack('I', socket.htonl(3232235787)))   # '192.168.1.11'
## 17、Python监控文件目录

    from watchdog.observers import Observer
    from watchdog.events import *
    import time


    class FileEventHandler(FileSystemEventHandler):
        def __init__(self):
            FileSystemEventHandler.__init__(self)

        def on_moved(self, event):
            if event.is_directory:
                print("directory moved from {0} to {1}".format(event.src_path,event.dest_path))
            else:
                print("file moved from {0} to {1}".format(event.src_path,event.dest_path))

        def on_created(self, event):
            if event.is_directory:
                print("directory created:{0}".format(event.src_path))
            else:
                print("file created:{0}".format(event.src_path))

        def on_deleted(self, event):
            if event.is_directory:
                print("directory deleted:{0}".format(event.src_path))
            else:
                print("file deleted:{0}".format(event.src_path))

        def on_modified(self, event):
            if event.is_directory:
                print("directory modified:{0}".format(event.src_path))
            else:
                print("file modified:{0}".format(event.src_path))


    if __name__ == "__main__":
        observer = Observer()
        event_handler = FileEventHandler()
        observer.schedule(event_handler, r"C:\Users\Liye\Desktop\ttt", True)
        observer.start()
        # try:
        #     while True:
        #         time.sleep(1)
        # except KeyboardInterrupt:
        #     observer.stop()
        observer.join()
        print('end...')
## 18、正则表达式匹配车牌
**利用正则表达式校验一个字符串是否是合法的车牌**

    import re 

    s1 = "浙AD12345*"
    s2 = "鄂A8P8F8D"
    s3 = ""
    s4 = "鄂A-8P8F8"
    regex = '^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领][A-Z][-]{0,1}[DF]?[A-Z0-9]{4}[A-Z0-9挂学警港澳领][DF]?$'
    print(re.match(regex,s1))
    print(re.match(regex,s2))
    print(re.match(regex,s3))
    print(re.match(regex,s4))
## 19、关于tuple
**答案：D**
* 不要把可变对象放在元组中。
* 增量赋值不是一个原子操作，虽然抛出了异常，但还是添加成功了。
![](https://github.com/daacheng/PythonBasic/blob/master/pic/tuple2.png)

## 20、Linux下创建Python虚拟环境
**python3 -m venv virtual-environment-name**</br>
* -m venv 选项的作用是以独立的脚本运行标准库中的 venv 包，后面的参数为虚拟环境的名称。

        # 创建
        python3 -m venv venv
        # 激活
        source venv/bin/activate
        # 退出
        deactivate
