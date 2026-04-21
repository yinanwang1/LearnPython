# 请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for nums in board:
            values = []
            for num in nums:
                if num != ".":
                    values.append(num)

            if self.hasDuplicateNumber(values):
                return False

        for i in range(9):
            values = []
            for j in range(9):
                v = board[j][i]
                if v != ".":
                    values.append(v)

            if self.hasDuplicateNumber(values):
                return False

        sArr = [(0, 0), (3, 0), (6, 0),
                (0, 3), (3, 3), (6, 3),
                (0, 6), (3, 6), (6, 6)]

        for i, j in sArr:
            values = []
            for s in range(3):
                for t in range(3):
                    v = board[s + i][t + j]
                    if v != ".":
                        values.append(v)

            if self.hasDuplicateNumber(values):
                return False

        return True

    def hasDuplicateNumber(self, nums: List[str]) -> bool:
        for num in nums:
            if nums.count(num) > 1:
                return True

        return False

