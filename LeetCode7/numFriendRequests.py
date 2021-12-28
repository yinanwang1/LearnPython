# There are n persons on a social media website. You are given an integer array ages
# where ages[i] is the age of the ith person.
# A Person x will not send a friend request to a person y (x != y)
# if any of the following conditions is true:
# age[y] <= 0.5 * age[x] + 7
# age[y] > age[x]
# age[y] > 100 && age[x] < 100
# Otherwise, x will send a friend request to y.
# Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.
# Return the total number of friend requests made.

from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        from collections import Counter
        r = 0
        counter = Counter(ages)
        keys = list(counter.keys())
        keys.sort()

        for i, k in enumerate(keys):
            if k < 15:
                continue
            n = counter[k]
            v = keys[i] * 0.5 + 7
            r += n * (n - 1)
            j = i - 1
            while j >= 0:
                if keys[j] <= v:
                    break

                r += n * counter[keys[j]]
                j -= 1

        return r




