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
