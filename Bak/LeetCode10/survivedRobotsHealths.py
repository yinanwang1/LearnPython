from typing import List

from sympy.physics.units.definitions import curie


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        idx = list(range(n))
        idx.sort(key=lambda index:positions[index])

        alive = []
        for i in idx:
            curIdx, curHel, curDir = i, healths[i], directions[i]
            while alive:
                preIdx, preHel, preDir = alive[-1]
                if preDir == "R" and curDir == "L":
                    alive.pop()
                    if preHel > curHel:
                        curIdx, curHel, curDir = preIdx, preHel-1, preDir
                    elif preHel < curHel:
                        curHel -= 1
                    else:
                        curIdx = -1
                        break
                else:
                    break
            if -1 != curIdx:
                alive.append((curIdx, curHel, curDir))

        alive.sort(key=lambda index: index[0])
        return [v[1] for v in alive]





if __name__ == '__main__':
    # positions = [5, 4, 3, 2, 1]
    # healths = [2, 17, 9, 15, 10]
    # directions = "RRRRR"
    # positions = [3,5,2,6]
    # healths = [10,10,15,12]
    # directions = "RLRL"
    positions = [2,19,46]
    healths = [42,45,2]
    directions = "LRL"
    solution = Solution()
    res = solution.survivedRobotsHealths(positions, healths, directions)
    print(res)




