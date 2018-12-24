import time
from progressbar import *

total = 1000


def dosomework():
    time.sleep(0.01)


def main():
    # progress = ProgressBar()
    # for i in progress(range(1000)):
    #     dosomework()
    pbar = ProgressBar().start()
    for i in range(1000):
        pbar.update(int((i / (total - 1)) * 100))
        dosomework()
    pbar.finish()


if __name__ == '__main__':
    main()