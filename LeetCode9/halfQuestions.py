
# 有 N 位扣友参加了微软与力扣举办了「以扣会友」线下活动。主办方提供了 2*N 道题目，整型数组 questions 中每个数字对应了
# 每道题目所涉及的知识点类型。
# 若每位扣友选择不同的一题，请返回被选的 N 道题目至少包含多少种知识点类型。

from typing import List

class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        from collections import Counter
        counter = Counter(questions)
        nums = list(counter.values())
        nums.sort(reverse=True)
        result, total, half = 0, 0, len(questions) // 2
        for v in nums:
            total += v
            result += 1
            if total >= half:
                return result
        return half

