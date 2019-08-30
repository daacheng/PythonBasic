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
* Publisher-Subscriber模式，消息是单向流动的，发布者只能发布消息，不能接受消息；订阅者只能接受消息，不能发送消息。
* 服务端发布消息过程中，如果有订阅者退出，不影响发布者继续发布消息，当订阅者再次连接上来，收到的消息是后来发布的消息。
* 比较晚加入的订阅者，或者中途离开的订阅者，必然会丢掉一部分信息。
* 如果发布者停止，所有订阅者会阻塞，等发布者再次上线的时候会继续接受消息。
* 订阅者必须使用zmq_setsockopt()方法来设置订阅的内容，否则将收不到任何消息。
* “慢连接”：我们不知道订阅者是何时开始接收消息的，就算先启动“订阅者”，再启动“发布者”，“订阅者”还是会缺失一部分消息，**因为建立连接是需要时间的，虽然很短，但不是零。ZMQ在后台是进行异步的IO传输，在建立TCP连接的短短的时间段内，ZMQ就可以发送很多消息了。**
* 有种简单的方法来同步“发布者”和“订阅者”，通过sleep让发布者延迟发送消息，等连接建立完成后再进行发送。

#### Publisher.py

    import zmq
    import time
    import random

    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")

    if __name__ == '__main__':
        print("发布者启动.....")
        time.sleep(2)
        for i in range(1000):
            tempterature = random.randint(-10, 40)
            message = "我是publisher, 这是我发布给你们的第{}个消息！今日温度{}".format(i+1, tempterature)
            socket.send_string(message)

#### Subscriber.py

    import zmq

    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5555")

    # 客户端需要设定一个过滤，否则收不到任何信息
    socket.setsockopt_string(zmq.SUBSCRIBE, '')

    if __name__ == '__main__':
        print('订阅者一号启动....')
        while True:
            message = socket.recv_string()
            print("（订阅者一号）接收到'发布者'发送的消息：{}".format(message))
