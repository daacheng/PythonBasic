from Getter import Getter
from Tester import Tester
import multiprocessing
import time

"""
    调度模块
"""
class Controller(object):

    """
        获取功能：爬取代理网站，将代理存储到redis
    """
    def control_get(self):
        getter = Getter()
        while True:
            getter.run()
            time.sleep(20)

    """
        检测功能，检测redis中的代理是否可用
    """
    def control_test(self):
        tester = Tester()
        while True:
            tester.run()
            time.sleep(20)

    def run(self):
        print('代理池开始运行了......')
        # 两个进程
        get = multiprocessing.Process(target=self.control_get)
        get.start()
        test = multiprocessing.Process(target=self.control_test)
        test.start()


if __name__ == '__main__':
    control = Controller()
    control.run()