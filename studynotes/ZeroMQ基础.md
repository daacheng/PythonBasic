# ZeroMQ基础
## 一、ZMQ的三种消息模式
### 1.1. Request-Reply（请求-应答模式）
* 使用Request-Reply模式，需要遵循一定的规律。
* 客户端必须先发送消息，再接收消息；服务端必须先进行接收客户端发送过来的消息，再发送应答给客户端。如此循环。
* 服务端和客户端谁先启动，效果都是一样的。
* 服务端在收到消息之前，会一直阻塞，等待客户端连上来。

#### 创建一个客户端和服务端，客户端发送Hello给服务端，服务端返回World给客户端
#### client.py

    import zmq

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    if __name__ == '__main__':
        print('zmq client start....')
        for i in range(1, 10):
            socket.send_string("hello")
            message = socket.recv()
            print('received reply message:{}'.format(message))

#### server.py

    import zmq
    import time

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    count = 0

    if __name__ == '__main__':
        print('zmq server start....')
        while True:
            message = socket.recv()
            count += 1
            print('received request. message:{} count:{}'.format(message, count))
            time.sleep(1)
            socket.send_string("World!")

### 1.2. Publisher-Subscriber(发布-订阅模式)
