#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python_syntax_review.py

用途：
    一个覆盖常见 Python 语法的复习文件。
    建议用法：
        1. 直接阅读
        2. 一段一段取消注释运行
        3. 用 PyCharm / VSCode 折叠代码块复习

说明：
    Python 语法非常多，这份文件覆盖日常开发最常用、面试最常考的核心语法。
"""

# ============================================================
# 01. 注释、变量、基本输出
# ============================================================

# 单行注释

"""
多行字符串，常用作模块、类、函数说明文档。
"""

name = "Python"
age = 30

print("Hello", name)
print(f"{name} 已经 {age} 岁了")


# ============================================================
# 02. 基本数据类型
# ============================================================

a = 10              # int
b = 3.14            # float
c = True            # bool
d = None            # NoneType
e = "hello"         # str
f = 1 + 2j          # complex

print(type(a), type(b), type(c), type(d), type(e), type(f))


# ============================================================
# 03. 类型转换
# ============================================================

print(int("123"))
print(float("3.14"))
print(str(100))
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False
print(bool("abc"))  # True


# ============================================================
# 04. 运算符
# ============================================================

x = 10
y = 3

print(x + y)    # 加
print(x - y)    # 减
print(x * y)    # 乘
print(x / y)    # 真除法
print(x // y)   # 整除
print(x % y)    # 取余
print(x ** y)   # 幂

print(x > y)
print(x == y)
print(x != y)

print(True and False)
print(True or False)
print(not True)

print(3 in [1, 2, 3])
print("py" in "python")


# ============================================================
# 05. 字符串
# ============================================================

s = "hello python"

print(s[0])
print(s[-1])
print(s[0:5])
print(s[:5])
print(s[6:])
print(s[::-1])

print(s.upper())
print(s.lower())
print(s.replace("python", "world"))
print(s.split(" "))
print("-".join(["a", "b", "c"]))

name = "Tom"
score = 95
print(f"{name} 的分数是 {score}")


# ============================================================
# 06. 列表 list
# ============================================================

nums = [1, 2, 3]

nums.append(4)
nums.insert(0, 0)
nums.remove(2)
last = nums.pop()

print(nums)
print(last)
print(nums[0])
print(nums[-1])
print(nums[0:2])

nums = [3, 1, 2]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)


# ============================================================
# 07. 元组 tuple
# ============================================================

point = (10, 20)

x, y = point
print(x, y)

single = (1,)
print(type(single))


# ============================================================
# 08. 字典 dict
# ============================================================

user = {
    "name": "Tom",
    "age": 18,
}

print(user["name"])
print(user.get("height", 0))

user["age"] = 20
user["city"] = "Hangzhou"

for key in user:
    print(key, user[key])

for key, value in user.items():
    print(key, value)


# ============================================================
# 09. 集合 set
# ============================================================

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 | s2)  # 并集
print(s1 & s2)  # 交集
print(s1 - s2)  # 差集
print(s1 ^ s2)  # 对称差集

s1.add(6)
s1.discard(2)
print(s1)


# ============================================================
# 10. 条件判断
# ============================================================

score = 85

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 三元表达式
result = "及格" if score >= 60 else "不及格"
print(result)


# ============================================================
# 11. for 循环
# ============================================================

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for index, value in enumerate(["a", "b", "c"]):
    print(index, value)

for a, b in zip([1, 2, 3], ["a", "b", "c"]):
    print(a, b)


# ============================================================
# 12. while 循环
# ============================================================

count = 0

while count < 3:
    print(count)
    count += 1


# ============================================================
# 13. break / continue / else
# ============================================================

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

# 循环正常结束时执行 else，遇到 break 不执行
for i in range(3):
    print(i)
else:
    print("循环正常结束")


# ============================================================
# 14. 推导式
# ============================================================

nums = [1, 2, 3, 4, 5]

squares = [x * x for x in nums]
even_squares = [x * x for x in nums if x % 2 == 0]

d = {x: x * x for x in nums}
s = {x * x for x in nums}

print(squares)
print(even_squares)
print(d)
print(s)


# ============================================================
# 15. 函数
# ============================================================

def add(a, b):
    return a + b

print(add(1, 2))


def greet(name="Python"):
    print(f"Hello {name}")

greet()
greet("Tom")


def calc(a, b):
    return a + b, a - b

sum_value, diff_value = calc(10, 3)
print(sum_value, diff_value)


# ============================================================
# 16. 函数参数
# ============================================================

def func(a, b=2, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

func(1, 3, 4, 5, name="Tom", age=18)


# 仅限关键字参数
def connect(host, *, port):
    print(host, port)

connect("localhost", port=3306)


# ============================================================
# 17. lambda 匿名函数
# ============================================================

add_lambda = lambda a, b: a + b
print(add_lambda(1, 2))

nums = [3, 1, 2]
nums.sort(key=lambda x: x)
print(nums)


# ============================================================
# 18. map / filter / sorted
# ============================================================

nums = [1, 2, 3, 4]

print(list(map(lambda x: x * 2, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))
print(sorted(nums, reverse=True))


# ============================================================
# 19. 作用域 global / nonlocal
# ============================================================

global_count = 0

def use_global():
    global global_count
    global_count += 1

use_global()
print(global_count)


def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner

counter = outer()
print(counter())
print(counter())


# ============================================================
# 20. 异常处理
# ============================================================

try:
    value = int("abc")
except ValueError as e:
    print("转换失败:", e)
else:
    print("没有异常时执行")
finally:
    print("无论是否异常都会执行")


def check_age(age):
    if age < 0:
        raise ValueError("年龄不能小于 0")
    return age

try:
    check_age(-1)
except ValueError as e:
    print(e)


# ============================================================
# 21. 文件操作
# ============================================================

file_path = "demo.txt"

with open(file_path, "w", encoding="utf-8") as f:
    f.write("hello\npython\n")

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)


# ============================================================
# 22. 面向对象 class
# ============================================================

class Person:
    species = "Human"  # 类变量

    def __init__(self, name, age):
        self.name = name      # 实例变量
        self.age = age

    def say_hello(self):
        print(f"我叫 {self.name}，今年 {self.age} 岁")

    @classmethod
    def create_baby(cls, name):
        return cls(name, 0)

    @staticmethod
    def is_adult(age):
        return age >= 18

p = Person("Tom", 18)
p.say_hello()

baby = Person.create_baby("Baby")
baby.say_hello()

print(Person.is_adult(20))


# ============================================================
# 23. 继承 / 重写 / super
# ============================================================

class Animal:
    def speak(self):
        print("动物叫")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("狗叫：汪汪")

dog = Dog()
dog.speak()


# ============================================================
# 24. 私有属性 / property
# ============================================================

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("余额不能为负数")
        self.__balance = value

account = BankAccount(100)
print(account.balance)
account.balance = 200
print(account.balance)


# ============================================================
# 25. 魔法方法
# ============================================================

class Node:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f"Node({self.val})"

    def __eq__(self, other):
        return isinstance(other, Node) and self.val == other.val

print(Node(1))
print(Node(1) == Node(1))


# ============================================================
# 26. dataclass
# ============================================================

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u = User("Tom", 18)
print(u)


# ============================================================
# 27. 类型注解
# ============================================================

from typing import List, Dict, Optional, Union, Callable, Any

def total(nums: List[int]) -> int:
    return sum(nums)

def find_user(user_id: int) -> Optional[Dict[str, Any]]:
    if user_id == 1:
        return {"id": 1, "name": "Tom"}
    return None

def handle(value: Union[int, str]) -> str:
    return str(value)

def run_callback(callback: Callable[[int], int]) -> int:
    return callback(10)

print(total([1, 2, 3]))
print(find_user(1))
print(handle("abc"))
print(run_callback(lambda x: x * 2))


# Python 3.9+ 常用写法
def total2(nums: list[int]) -> int:
    return sum(nums)


# ============================================================
# 28. 枚举 Enum
# ============================================================

from enum import Enum

class Status(Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

status = Status.SUCCESS
print(status)
print(status.name)
print(status.value)


# ============================================================
# 29. 迭代器
# ============================================================

class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for i in CountDown(3):
    print(i)


# ============================================================
# 30. 生成器 yield
# ============================================================

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for i in count_up_to(3):
    print(i)


# ============================================================
# 31. 装饰器
# ============================================================

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时: {end - start:.6f}s")
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(0.1)
    return a + b

print(slow_add(1, 2))


# ============================================================
# 32. 上下文管理器
# ============================================================

class MyContext:
    def __enter__(self):
        print("进入上下文")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出上下文")

with MyContext():
    print("执行代码")


from contextlib import contextmanager

@contextmanager
def simple_context():
    print("开始")
    yield
    print("结束")

with simple_context():
    print("中间执行")


# ============================================================
# 33. 模块导入
# ============================================================

import math
import os
from pathlib import Path
from collections import defaultdict, Counter, deque

print(math.sqrt(16))
print(os.getcwd())
print(Path(".").resolve())

counter = Counter(["a", "b", "a"])
print(counter)

d = defaultdict(int)
d["a"] += 1
print(d)

queue = deque([1, 2, 3])
queue.append(4)
queue.popleft()
print(queue)


# ============================================================
# 34. 包和模块
# ============================================================

"""
模块：一个 .py 文件就是一个模块。
包：包含 __init__.py 的目录就是一个包。

示例：
    my_package/
        __init__.py
        utils.py

导入：
    import my_package.utils
    from my_package import utils
"""


# ============================================================
# 35. 日期时间
# ============================================================

from datetime import datetime, date, timedelta

now = datetime.now()
today = date.today()
tomorrow = today + timedelta(days=1)

print(now)
print(today)
print(tomorrow)
print(now.strftime("%Y-%m-%d %H:%M:%S"))

dt = datetime.strptime("2026-06-15", "%Y-%m-%d")
print(dt)


# ============================================================
# 36. JSON
# ============================================================

import json

data = {"name": "Tom", "age": 18}

json_str = json.dumps(data, ensure_ascii=False)
print(json_str)

obj = json.loads(json_str)
print(obj)


# ============================================================
# 37. 正则表达式
# ============================================================

import re

text = "phone: 13812345678"

match = re.search(r"\d{11}", text)
if match:
    print(match.group())

print(re.findall(r"\d+", "a1 b22 c333"))
print(re.sub(r"\d+", "*", "a1 b22 c333"))


# ============================================================
# 38. 常用内置函数
# ============================================================

nums = [1, 2, 3, 4]

print(len(nums))
print(sum(nums))
print(max(nums))
print(min(nums))
print(abs(-10))
print(round(3.14159, 2))
print(any([False, True]))
print(all([True, True]))
print(list(reversed(nums)))


# ============================================================
# 39. 解包
# ============================================================

a, b = 1, 2
a, b = b, a
print(a, b)

first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)

d1 = {"a": 1}
d2 = {"b": 2}
d3 = {**d1, **d2}
print(d3)

list1 = [1, 2]
list2 = [3, 4]
list3 = [*list1, *list2]
print(list3)


# ============================================================
# 40. match case，Python 3.10+
# ============================================================

command = "start"

match command:
    case "start":
        print("启动")
    case "stop":
        print("停止")
    case _:
        print("未知命令")


# ============================================================
# 41. 海象运算符，Python 3.8+
# ============================================================

if (n := len("python")) > 3:
    print(n)


# ============================================================
# 42. async / await 异步
# ============================================================

import asyncio

async def fetch_data():
    await asyncio.sleep(0.1)
    return "data"

async def main_async():
    result = await fetch_data()
    print(result)

asyncio.run(main_async())


# ============================================================
# 43. 多线程
# ============================================================

from threading import Thread

def worker(name):
    print(f"线程 {name} 执行")

t = Thread(target=worker, args=("A",))
t.start()
t.join()


# ============================================================
# 44. 线程池
# ============================================================

from concurrent.futures import ThreadPoolExecutor

def task(x):
    return x * x

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(task, [1, 2, 3, 4]))
    print(results)


# ============================================================
# 45. 多进程
# ============================================================

from multiprocessing import Process

def process_worker():
    print("子进程执行")

# Windows/macOS 下多进程建议放到 if __name__ == "__main__" 中
# p = Process(target=process_worker)
# p.start()
# p.join()


# ============================================================
# 46. argparse 命令行参数
# ============================================================

"""
示例：

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="Python")
args = parser.parse_args()

print(args.name)

命令行运行：
    python python_syntax_review.py --name Tom
"""


# ============================================================
# 47. 常见算法语法模板
# ============================================================

# 栈
stack = []
stack.append(1)
stack.append(2)
print(stack.pop())

# 队列
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
print(queue.popleft())

# 哈希表
hash_map = {}
hash_map["a"] = 1
print(hash_map.get("a", 0))

# DFS
graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: [],
}

def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    print(node)
    for nxt in graph[node]:
        dfs(nxt, visited)

dfs(1, set())

# BFS
def bfs(start):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node)

        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)

bfs(1)


# ============================================================
# 48. main 入口
# ============================================================

def main():
    print("程序入口")

if __name__ == "__main__":
    main()
