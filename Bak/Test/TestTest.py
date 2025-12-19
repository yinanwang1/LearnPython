from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

with tag("h1"):
    print("This is Ttitle")



# Python 像JS一样支持一个变量多种类型
class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None