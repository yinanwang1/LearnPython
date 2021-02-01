class Solution:
    def countLargestGroup(self, n: int) -> int:
        numsDic = dict()
        for i in range(1, n+1):
            key = i
            if i > 9:
                key = sum([int(x) for x in list(str(i))])
            value = numsDic.get(key, 0)
            numsDic[key] = value

        maxValue = 1
        maxValueNums = 0
        for value in numsDic.values():
            if maxValue == value:
                maxValueNums += 1
            elif maxValue < value:
                maxValue = value
                maxValueNums = 1

        return maxValueNums
