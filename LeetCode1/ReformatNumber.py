class Solution:
    def reformatNumber(self, number: str) -> str:
        lists = list()
        temp = ''

        for value in number:
            if value != ' ' and value != '-':
                temp += value
                if 3 == len(temp):
                    lists.append(temp)
                    temp = ''
        if len(temp) > 0:
            lists.append(temp)
        if 1 < len(lists) and 1 == len(lists[-1]):
            lists[-1] = lists[-2][2] + lists[-1]
            lists[-2] = lists[-2][:2]

        return '-'.join(lists)