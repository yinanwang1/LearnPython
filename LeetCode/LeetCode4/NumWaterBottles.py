class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        temp = numBottles

        while temp >= numExchange:
            result += int(temp / numExchange)
            temp = int(temp / numExchange) + temp % numExchange

        return result