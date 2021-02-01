from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = list()
        for col in range(0, len(mat[0])):
            for row in range(len(mat)):
                if 0 == mat[row][col] and row not in result:
                    result.append(row)
                    if k <= len(result):
                        return result
        index = 0
        while k > len(result):
            if index not in result:
                result.append(index)

            index += 1

        return result


power = [1, 4, 3]
ans = [0, 1, 2]
ans.sort(key=lambda i: power[i])
print(ans)