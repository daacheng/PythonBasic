import os
import shutil

"""
todo 瓜子二手车数据爬取
"""

def main():
    path = r'C:\aaa.txt'
    # os.rename(path, r'E:\aaaa.txt')
    shutil.move(path, r'E:\aaaa.txt')


if __name__ == '__main__':
    main()