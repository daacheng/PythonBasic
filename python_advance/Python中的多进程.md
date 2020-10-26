## 创建多进程

```python
import multiprocessing  
import os  
def hello(arg):  
    print('父进程id-{} 子进程id-{}  arg-{}'.format(os.getppid(), os.getpid(), arg))  
if __name__ == '__main__':  
    for i in range(3):  
        p = multiprocessing.Process(target=hello, args=(i,))  
        p.start()  
        p.join()  
# 结果  
父进程id-14940 子进程id-11464  arg-0  
父进程id-14940 子进程id-13808  arg-1  
父进程id-14940 子进程id-9976  arg-2  
```

## 通过信号量控制进程的退出 kill 15 pid
```python
import multiprocessing
import os
import re
import logging.handlers
import time
import signal


def term(sig_num, addtion):
    mylog.info('term current pid is %s, group id is %s' % (os.getpid(), os.getpgrp()))
    os.killpg(os.getpgid(os.getpid()), signal.SIGKILL)


def log_record(log_filename):
    """
        日志模块配置
        CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
    """
    dir_path = os.path.split(__file__)[0]
    logdir = os.path.join(dir_path, 'log')
    try:
        os.makedirs(logdir, exist_ok=True)
    except FileExistsError:
        pass

    myapp = logging.getLogger(os.path.basename(log_filename))
    myapp.setLevel(logging.DEBUG)
    # 按照每天一个日志，保留最近14个
    filehandler = logging.handlers.TimedRotatingFileHandler(
        filename='%s/%s' % (logdir, os.path.basename(log_filename)),
        when='midnight', interval=1, backupCount=14)
    filehandler.suffix = '%Y%m%d.log'
    filehandler.extMatch = re.compile(r'^\d{8}.log$')  # 只有填写了此变量才能删除旧日志
    filehandler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    myapp.addHandler(filehandler)
    # 让日志输出到console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    myapp.addHandler(console)
    return myapp

process_list = []
mylog = log_record('test')


class DataDeal(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        pass

    def run(self):
        while True:
            mylog.info('ID:{} running....'.format(os.getpid()))
            time.sleep(3)


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, term)
    mylog.info('主进程ID:{}'.format(os.getpid()))

    for _ in range(3):
        p = DataDeal()
        process_list.append(p)

    mylog.info(process_list)
    for p in process_list:
        p.daemon = True
        p.start()

    for p in process_list:
        p.join()

```

## 进程间共享变量
每个进程都有自己的独立内存空间，进程中的变量都是相互独立的。如下所示，修改子进程中变量的值，主进程中变量并不会改变。

```python
import multiprocessing  
n = 0  
def hello():  
    global n  
    n += 1  
    print('子进程-n: {}'.format(n))  

if __name__ == '__main__':  
    p = multiprocessing.Process(target=hello)  
    p.start()  
    p.join()  
    print('主进程-n: {}'.format(n))  
# 结果  
子进程-n: 1  
主进程-n: 0  
```
要实现进程间的变量共享，multiprocessing.Value定义变量，传参的形式实现进程间变量共享。


```python
import multiprocessing  
n = multiprocessing.Value('i', 0)  
def hello(n):  
    n.value += 1  
    print('子进程-n: {}'.format(n.value))  
if __name__ == '__main__':  
    p = multiprocessing.Process(target=hello, args=(n,))  
    p.start()  
    p.join()  
    print('主进程-n: {}'.format(n.value))  
# 结果  
子进程-n: 1  
主进程-n: 1
```
