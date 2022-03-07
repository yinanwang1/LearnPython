

# You are given an integer array score of size n, where score[i] is the score of the ith athlete
# in a competition. All the scores are guaranteed to be unique.
# The athletes are placed based on their scores, where the 1st place athlete has the highest score,
# the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number
# (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.

from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scoreMap, result = {}, ["0" for _ in range(len(score))]
        for i, v in enumerate(score):
            scoreMap[v] = i
        score.sort(reverse=True)
        for i, v in enumerate(score):
            index = scoreMap.get(v)
            if 0 == i:
                result[index] = "Gold Medal"
            elif 1 == i:
                result[index] = "Silver Medal"
            elif 2 == i:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(i + 1)

        return result
