# Python十进制、十六进制、字节串、字符串转换

## 整数之间进制转换

        #十进制转换成十六进制
        hex(10)    #'0xa'
        hex(11)    #'0xb'
        hex(15)    #'0xf'

        #十六进制转换为十进制
        int('0xa',16)         #10
        int('ff',16)          #255
        int('f',16)           #15

        #十进制转换成二进制
        bin(2)                #'0b10'
        bin(255)              #'0b11111111'
        bin(8)                #'0b1000'

        #十进制转换成八进制
        oct(8)                #'0o10'
        oct(7)                #'0o7'
        oct(9)                #'0o11'

## 字符串转换成整数

        #十进制字符串转整数
        int('10')             #10
        int('20')             #20

        #十六进制字符串转整数
        int('f',16)           #15
        int('ff',16)          #255
        int('a',16)           #10
        int('11',16)          #17

        #二进制字符串转整数
        int('1000',2)         #8
        int('1001',2)         #9

        #字节串转整数
        import struct
        struct.unpack('>II',bytes(b'\x01\x00\x00\x00\x01\x00\x00\x00'))             #(16777216, 16777216)

        #整数转换成字节串
        struct.pack('>II',16777216, 16777216)                                       #b'\x01\x00\x00\x00\x01\x00\x00\x00'

## 字符串转字节串

        #字符串编码为字节码
        '123abc'.encode('ascii')                  #b'123abc'
        '123abc'.encode('utf-8')                  #b'123abc'
        '123abc好'.encode('utf-8')                #b'123abc\xe5\xa5\xbd'

        #十六进制字符串转字节串
        bytes.fromhex('ff011a')                   #b'\xff\x01\x1a'
        #十六进制字符串转字节串
        bytes(map(ord,'\xff\x01\x1a'))            #b'\xff\x01\x1a'
        #十六进制数组转字节串
        bytes([0x01,0x02,0x03,0xff])              #b'\x01\x02\x03\xff'

## 字节串转字符串

        #字节码解码为字符串
        bytes(b'123abc\xe5\xa5\xbd').decode('utf-8')         #'123abc好'
        #字节串转16进制表示
        str(bytes(b'123abc\xe5\xa5\xbd'))                    #"b'123abc\\xe5\\xa5\\xbd'"
        str(bytes(b'123abc\xe5\xa5\xbd'))[2:-1]              #'123abc\\xe5\\xa5\\xbd'
        #字节串转换成16进制数组
        [hex(i) for i in bytes(b'123')]                      #['0x31', '0x32', '0x33']
