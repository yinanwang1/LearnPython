from typing import List

class OrderedStream:

    def __init__(self, n: int):
        self.datasource = [''] * n
        self.index = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.datasource[id - 1] = value
        tempList = list()
        while self.index < len(self.datasource) and self.datasource[self.index - 1] is not '':
            tempList.append(value)
            self.index += 1
        
        return tempList




# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)