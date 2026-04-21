class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dataSource = list()


    def push(self, x: int) -> None:
        self.dataSource.append(x)


    def pop(self) -> None:
        self.dataSource.pop(0)

    def top(self) -> int:
        return self.dataSource[-1]

    def getMin(self) -> int:
        return min(self.dataSource)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()