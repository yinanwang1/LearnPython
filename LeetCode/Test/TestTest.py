import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor
from contextlib import contextmanager
from functools import wraps

from LeetCode.LeetCode4 import RepeatedNTimes


def task(x):
    print(

        f"x={x}, "

        f"线程={threading.current_thread().name}"

    )

    time.sleep(2)

    return x * x

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时 {end - start} 秒")
        return result

    return wrapper

@timer
def my_func():
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(task, [1, 2, 3, 4]))

    return results


print(my_func())