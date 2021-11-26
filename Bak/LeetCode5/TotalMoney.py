class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        day = 1
        monday = 1

        while day <= n:
            for i in range(7):
                total += monday + i

                day += 1
                monday += 1
                if day > n:
                    break

        return total

