## 1.时间转换成指定格式

    import time 
    time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    time.localtime(time.time())
    # time.struct_time(tm_year=2018, tm_mon=5, tm_mday=16, tm_hour=10, tm_min=21, tm_sec=2, tm_wday=2, tm_yday=136, tm_isdst=0)

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

6.创建临时文件

    import tempfile
    import os
    tmpfd, tmp_file_path = tempfile.mkstemp()
    print(tmpfd)   #文件描述符
    print(tmp_file_path)   #临时文件的绝对路径
    os.close(tmpfd)   #关闭文件

    # 防止占用资源
    tempfile.mktemp()  #mktemp用于返回一个临时文件的路径，但并不创建该临时文件。
