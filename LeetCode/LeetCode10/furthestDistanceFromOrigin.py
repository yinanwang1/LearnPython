
# 2833. 距离原点最远的点
# https://leetcode.cn/problems/furthest-point-from-origin?envType=daily-question&envId=2026-04-24&status=NOT_STARTED&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJBQ19SQVRFIn1d&difficulty=EASY


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left, right = 0, 0
        for move in moves:
            if move == 'L':
                left += 1
            elif move == 'R':
                right += 1
            else:
                pass
        return  abs(left - right) + len(moves) - left - right


if __name__ == '__main__':
    # print(Solution().furthestDistanceFromOrigin("L_RL__R"))
    # print(Solution().furthestDistanceFromOrigin("_R__LL_"))
    print(Solution().furthestDistanceFromOrigin("_" * 50))
