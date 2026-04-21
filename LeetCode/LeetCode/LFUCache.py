class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.valueDict = dict()
        self.timesDict = dict()
        self.keysList = list()

    def get(self, key: int) -> int:
        if key not in self.keysList:
            return -1

        value = self.valueDict[key]
        times = self.timesDict[key] + 1
        self.timesDict[key] = times
        self.keysList.remove(key)
        self.move(key, times)

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.keysList:
            self.valueDict[key] = value

            times = self.timesDict[key] + 1
            self.timesDict[key] = times
            self.keysList.remove(key)
            self.move(key, times)

            return

        if len(self.keysList) >= self.capacity:
            lasttKey = self.keysList.pop()
            self.timesDict.pop(lasttKey)
            self.valueDict.pop(lasttKey)

        self.valueDict[key] = value
        self.timesDict[key] = 1
        self.move(key, 1)

    def move(self, key, times):
        hasInsert = False
        for index, item in enumerate(self.keysList):
            itemTimes = self.timesDict[item]
            if times >= itemTimes:
                hasInsert = True
                self.keysList.insert(index, key)
                break

        if hasInsert is False:
            self.keysList.append(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)