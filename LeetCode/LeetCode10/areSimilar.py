from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if 1 == i % 2:
                    if mat[i][j] != mat[i][(j + k) % n]:
                        return False
                else:
                    if mat[i][j] != mat[i][(j - k + n) % n]:
                        return False
        return True
