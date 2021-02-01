from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if 0 == rowIndex:
            return []
        if rowIndex == 1:
            return [1]
        index = 2
        rowList = [1, 1]

        while index <= rowIndex:
            rowListTemp = [1]
            for i in range(len(rowList) - 1):
                rowListTemp.append(rowList[i] + rowList[i+1])
            rowListTemp.append(1)

            rowList = rowListTemp
            index += 1

        return rowList

