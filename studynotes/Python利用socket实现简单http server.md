# 利用socket实现http协议

**http协议是基于tcp的，所以利用tcp可以实现http协议，实现一个简单的 http web server功能。**

        import socketserver


        body = """<h1>hello web client</h1>"""

        response_param = ['HTTP/1.0 200 OK',
                          'Date: Mon, 13 May 2019 09:57:18 GMT',
                          'Content-Type: text/html; charset=utf-8',
                          'Content-Length: {}\r\n'.format(len(body.encode())),
                          body]
        response = '\r\n'.join(response_param)


        class MyServer(socketserver.BaseRequestHandler):
            def handle(self):
                conn = self.request
                recv_data = b''
                while b'\n\n' not in recv_data and b'\n\r\n' not in recv_data:

                    recv_data += conn.recv(1024)
                print(recv_data)
                conn.send(response.encode())
                conn.close()


        if __name__ == '__main__':
            # 第一步
            # 实例化server对象，传入本机ip，以及监听的端口号，还有新建的继承socketserver模块下的BaseRequestHandler类
            server = socketserver.ThreadingTCPServer(('127.0.0.1', 8000), MyServer)
            # 激活服务端
            server.serve_forever()
