from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        result = [[10000] * n for _ in range(m)]
        remain = list()

        for row in range(m):
            for column in range(n):
                if matrix[row][column] == 0:
                    result[row][column] = 0
                else:
                    remain.append((row, column))

        times = 0
        while len(remain) > 0:
            print('Enter')
            print(remain)
            remainTemp = remain.copy()

            for row, column in remainTemp:
                for rowTemp, columnTemp in [(row, column - 1), (row + 1, column), (row, column + 1), (row - 1, column)]:
                    if 0 <= rowTemp < m and 0 <= columnTemp < n:
                        if result[rowTemp][columnTemp] == times:
                            result[row][column] = times + 1
                            remain.remove((row, column))
                            break

            print('Exit')
            print(remain)

            times += 1


        return result


solution = Solution()
result = solution.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
print('END')
print(result)



