# Python通用日志模块配置

    import os
    import logging.handlers
    import re

    """
        通用日志配置,代码copy过来直接使用mylog对象即可
    """
    # 日志模块配置
    # CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
    # 创建log日志文件夹
    dir_path = os.path.split(__file__)[0]
    logdir = os.path.join(dir_path, 'log')
    try:
        os.makedirs(logdir, exist_ok=True)
    except FileExistsError:
        pass
    module_name = os.path.basename(__file__).replace('.py', '')
    mylog = logging.getLogger(__name__)
    mylog.setLevel(logging.DEBUG)
    # 按照每天一个日志，保留最近14个
    filehandler = logging.handlers.TimedRotatingFileHandler(
        filename='%s/%s' % (logdir, module_name),
        when='midnight', interval=1, backupCount=14)
    filehandler.suffix = '%Y%m%d.log'
    filehandler.extMatch = re.compile(r'^\d{8}.log$')  # 只有填写了此变量才能删除旧日志
    # 日志打印格式
    filehandler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    mylog.addHandler(filehandler)
    # 让日志输出到console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    mylog.addHandler(console)


    def main():
        mylog.info('hello,this is my own log.')
        mylog.error('you have an error in you code!')


    if __name__ == '__main__':
        main()
