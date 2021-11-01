class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        sum = n
        nums = list()

        while sum != 1:
            if sum in nums:
                break
            nums.append(sum)
            sumTmep = 0
            for num in str(sum):
                sumTmep += int(num) * int(num)

            sum = sumTmep

        return sum == 1