class Solution:
    def countAndSay(self, n: int) -> str:
        if 1 == n:
            return '1'

        def countString(string: str) -> str:
            char = 'a'
            count = 0
            result = ''
            for c in string:
                if char == 'a':
                    char = c
                    count = 1
                elif char == c:
                    count += 1
                else:
                    result += '{}{}'.format(count, char)
                    char = c
                    count = 1
            if char != 'a':
                result += '{}{}'.format(count, char)

            return result

        sum = '1'
        for _ in range(n - 1):
            sum = countString(sum)

        return sum



