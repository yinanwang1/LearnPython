class Solution:
    def myAtoi(self, str: str) -> int:
        no_space_str = str.strip()
        if 0 >= len(no_space_str):
            return 0

        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbol = ['-', '+'] + nums

        first = no_space_str[0]
        if first not in symbol:
            return 0

        result = first
        for index in range(1, len(no_space_str)):
            character = no_space_str[index]
            if character in nums:
                result += character
            else:
                break

        try:
            result_int = int(result)
        except ValueError:
            return 0

        if result_int < -2147483648:
            return -2147483648
        if result_int > 2147483647:
            return 2147483647

        return result_int







