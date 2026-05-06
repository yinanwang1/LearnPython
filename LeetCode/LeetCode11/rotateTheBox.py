from typing import List


# 1861. 旋转盒子
# https://leetcode.cn/problems/rotating-the-box/description/

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        result = list()
        for v in zip(*boxGrid):
            result.append(list(v[::-1]))
        m, n = len(result), len(result[0])
        for j in range(n):
            for i in range(m - 1, -1, -1):
                v = result[i][j]
                if '#' == v or '*' == v:
                    continue
                else:
                    # 查找石头，遇到障碍物结束
                    for k in range(i-1, -1, -1):
                        pre_v = result[k][j]
                        if '#' == pre_v:
                            result[k][j] = '.'
                            result[i][j] = '#'
                            break
                        elif '*' == pre_v:
                            break
        return result


if __name__ == '__main__':
    print(Solution().rotateTheBox(boxGrid=[["#",".","#"]]))

