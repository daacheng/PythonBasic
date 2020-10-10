## concurrent.futures模块
python标准库为我们提供了concurrent.futures模块，它提供了ThreadPoolExecutor和ProcessPoolExecutor两个类，实现了对threading和multiprocessing的更高级的抽象，对编写线程池/进程池提供了直接的支持。
#### 1.单线程下载任务
```python
import time
import requests

def download(index, pic_url):
    resp = requests.get(pic_url)
    with open('down.png', 'wb') as fw:
        fw.write(resp.content)
    return index

if __name__ == '__main__':
    url = 'https://github.com/daacheng/PythonBasic/blob/master/pic/python_basic/tuple2.png'
    urls = [(index, url) for index in range(1, 6)]
    t0 = time.time()
    for index, pic_url in urls:
        res = download(index, pic_url)
        print('下载成功-{}'.format(res))
    elapsed = time.time() - t0
    print('下载耗时: {}'.format(elapsed))
```
运行结果
```python
下载成功-1
下载成功-2
下载成功-3
下载成功-4
下载成功-5
下载耗时: 3.3739817142486572
```

#### 2.使用concurrent.futures的多线程下载任务
#### 方式一：主要是concurrent.futures.Executor对象和concurrent.futures.Future对象
1. **futures.ThreadPoolExecutor(workers)** 创建线程池Executor对象，指定工作线程的数量。
2. **executor.submit(download, index, pic_url)** 把任务交给concurrent.futures.Executor对象，通过executor.submit() 创建concurrent.futures.Future对象。
3. **futures.as_completed(todo)** concurrent.futures.as_completed函数的参数是一个Future对象列表，返回值是一个迭代器，在Future对象运行结束后返回Future对象。
4. future.result(timeout)方法,会阻塞调用方所在的线程，直到有结果可返回.

```python
import time
import requests
from concurrent import futures

def download(index, pic_url):
    resp = requests.get(pic_url)
    with open('down.png', 'wb') as fw:
        fw.write(resp.content)
    return index

if __name__ == '__main__':
    url = 'https://github.com/daacheng/PythonBasic/blob/master/pic/python_basic/tuple2.png'
    urls = [(index, url) for index in range(1, 6)]
    workers = len(urls)
    t0 = time.time()
    with futures.ThreadPoolExecutor(workers) as executor:
        todo = {executor.submit(download, index, pic_url) for index, pic_url in urls}
        for future in futures.as_completed(todo):
            # 本示例中调用future.result()方法绝不会阻塞，因为future是由as_completed函数产出。
            res = future.result()
            print('下载成功-{}'.format(res))

    elapsed = time.time() - t0
    print('下载耗时: {}'.format(elapsed))
```
运行结果
```python
下载成功-4
下载成功-3
下载成功-2
下载成功-5
下载成功-1
下载耗时: 0.7290542125701904
```

#### 方式二
executor.map()方法的作用与内置的map函数类似，download函数会在多个线程中并发调用, map方法返回一个生成器，因此可以迭代，获取各个线程返回的值。

```python
import time
import requests
from concurrent import futures

def download(index, url):
    resp = requests.get(url)
    with open('down.png', 'wb') as fw:
        fw.write(resp.content)
    return index

if __name__ == '__main__':
    url = 'https://github.com/daacheng/PythonBasic/blob/master/pic/python_basic/tuple2.png'
    urls = [(index, url) for index in range(1, 6)]
    workers = len(urls)
    t0 = time.time()
    with futures.ThreadPoolExecutor(workers) as executor:
        download_tasks_res = executor.map(download, (i[0] for i in urls), (i[1] for i in urls))

        for res in download_tasks_res:
            print('下载成功-{}'.format(res))

    elapsed = time.time() - t0
    print('下载耗时: {}'.format(elapsed))
```
运行结果
```python
下载成功-1
下载成功-2
下载成功-3
下载成功-4
下载成功-5
下载耗时: 0.5195839405059814
```


#### 3. futures.ProcessPoolExecutor与futures.ThreadPoolExecutor的用法类似
对CPU密集型工作来说，要启动多个进程，规避GIL。创建多个进程最简单的方式是用futures.ProcessPoolExecutor 类。对于比较复杂的多线程，多进程使用场景，还是要用threading和multiprocessing来替代futures.ThreadPoolExecutor和futures.ProcessPoolExecutor。
