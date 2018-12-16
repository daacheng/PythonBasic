from queue import Queue

q = Queue()
def main():
    while True:
        try:
            item = q.get(block=True, timeout=10)
        except Exception as e:
            break

    print('队列长时间为空，结束循环')


if __name__ == '__main__':
    main()