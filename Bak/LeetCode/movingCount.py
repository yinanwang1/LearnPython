class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        result = set()
        passed = set()

        def move(x: int, y: int):
            if (x, y) in passed:
                return

            passed.add((x, y))

            str_list = list(str(x)) + list(str(y))
            nums_list = map(lambda s: int(s), str_list)

            if k >= sum(nums_list):
                result.add((x, y))
            else:
                return

            for i, j in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                if 0 <= i < m and 0 <= j < n:
                    move(i, j)

        move(0, 0)

        return len(result)



solution = Solution()
# result = solution.movingCount(1, 2, 1)
# result = solution.movingCount(2, 3, 1)
# result = solution.movingCount(3, 1, 0)
result = solution.movingCount(16, 8, 4)
print('END')
print(result)

