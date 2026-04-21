import threading
import time
from enum import Enum


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def worker(name):
    print("Worker %s start" % name)
    time.sleep(1)
    print("Worker %s done" % name)


if __name__ == '__main__':
    print('start')

    print('thread start')
    t1 = threading.Thread(target=worker, args=("worker1",))
    t1.start()  # 启动线程
    t1.join()  # 等待线程结束
    print('thread end')

    print('end')
