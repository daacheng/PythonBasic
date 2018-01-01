"""
    这个函数接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，
    以及其包含文件夹中文件的路径。

"""
import os
def print_directory_contents(sPath):
    import os
    for sChild in os.listdir(sPath):    #指定路径下的文件和文件夹名['.ipynb_checkpoints', 'python1.ipynb']
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)#如果path路径下是文件夹，则继续找出该文件夹下的所有文件名
        else:
            print(sChildPath)
#print_directory_contents('D:\daacheng\Python\PythonCode\pythontest')
path='D:\daacheng\Python\PythonCode\pythontest'
print_directory_contents(path)