class Solution:
    def exchangeBits(self, num: int) -> int:
        num_str = bin(num)
        num_str = num_str.replace('0b', '')
        if len(num_str) % 2 != 0:
            num_str = '0' + num_str
        odd = num_str[1::2]
        even = num_str[0::2]
        result = ''

        print(num_str)
        print(odd)
        print(even)

        for index in range(len(odd)):
            result += odd[index]
            result += even[index]

        print('result')
        print(result)

        return int('0b' + result, 2)


solution = Solution()
result = solution.exchangeBits(21)
print('end')
print(result)