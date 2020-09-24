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
