
# Alice has some number of cards and she wants to rearrange the cards into groups so that
# each group is of size groupSize, and consists of groupSize consecutive cards.
# Given an integer array hand where hand[i] is the value written on the ith card
# and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if 0 != len(hand) % groupSize:
            return False
        from collections import Counter
        # 数字为key和个数为value
        counter = Counter(hand)
        hand.sort()

        for k in hand:
            if counter[k] == 0:
                continue
            for v in range(k, k + groupSize):
                if 0 == counter[v]:
                    return False
                counter[v] -= 1

        return True




