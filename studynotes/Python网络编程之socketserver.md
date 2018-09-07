## 服务器端(TCP)
1. 创建socket对象，绑定IP和端口进行监控（socketserver对象对socket对象进行了封装，不需要再bind() listen() accept()）
2. 服务器端阻塞,直到有客户端连接进来
3. 客户端连接进来后，开始进行通信。


        import socketserver

        #创建一个socketserver类继承socketserver模块下的BaseRequestHandler类
        class MyServer(socketserver.BaseRequestHandler):
            def handle(self):
                # 第二部：服务器端阻塞，等待客户端连接
                #重写父类中的handle方法，主要实现服务端的逻辑代码，，不用写bind() listen() accept()
                while True:
                    conn = self.request
                    addr = self.client_address
                    print(conn)  #<socket.socket fd=864, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9999), raddr=('127.0.0.1', 50565)>
                    print(addr)  #('127.0.0.1', 50565)
                    # 第三步：服务器端与客户端进行通信
                    #接收到来自客户端的数据
                    recv_data = str(conn.recv(1024),encoding = 'utf8')
                    print(recv_data)
                    #如果客户端发送的是‘bye’就断开连接 
                    if recv_data == 'bye':
                        break

                    #服务器端回复数据给客户端
                    send_data =  bytes(input('请输入回复消息：'),encoding = 'utf8')
                    conn.sendall(send_data)

                conn.close()
        if __name__ == '__main__':
            # 第一步
            #实例化server对象，传入本机ip，以及监听的端口号，还有新建的继承socketserver模块下的BaseRequestHandler类
            server = socketserver.ThreadingTCPServer(('127.0.0.1',9999),MyServer)  
            #激活服务端
            server.serve_forever()

## 客户端(TCP)
1. 创建socket对象
2. 指定IP和端口，建立连接
3. 连接成功后，开始通信。

        import socket

        #创建一个socket对象，指定要连接的目标服务器 ip及端口号
        # 第一步
        s =  socket.socket()
        s.connect(('127.0.0.1',9999))
        while True:

            #连接成功后向服务器端发送数据 
            send_data = input('请输入需要发送的内容')
            s.sendall(bytes(send_data,encoding = 'utf8'))
            if send_data=='bye':
                break

            #客户端接收来自服务器端发送的数据
            recv_data =  str(s.recv(1024),encoding='utf8')
            print(recv_data)
        s.close()

## 服务端(UDP)

        import socketserver
        import time
        class MyServer(socketserver.BaseRequestHandler):
            def handle(self):
                while True:
                    data = self.request[0].strip()
                    socket = self.request[1]
                    print('客户端IP：',self.client_address[0])    # 192.168.141.1
                    socket.sendto(data, self.client_address)
                    time.sleep(2)

                conn.close()
        if __name__ == '__main__':
            server = socketserver.ThreadingUDPServer(('0.0.0.0',9999),MyServer)
            print('servering……')
            server.serve_forever()

## 客户端(UDP)
1. 创建socket对象
2. 直接往指定IP和端口发送数据

        import socket
        import time
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        while True:
            send_data = '111111111111111111111111111111111111'
            print(send_data)
            s.sendto(bytes(send_data,encoding = 'utf8'),('127.0.0.1',9999))    
            #客户端接收来自服务器端发送的数据
            recv_data =  str(s.recv(1024),encoding='utf8')
            print(recv_data)  
            time.sleep(2)
        s.close()
