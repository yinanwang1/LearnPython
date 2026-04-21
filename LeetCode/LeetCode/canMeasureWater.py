class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z in [0, x, y, (x + y), abs(x - y)]:
            return True

        attribute = {x, y, abs(x - y)}
        pre_length = len(attribute)
        whole_nums = list(attribute)

        while True:
            minus_list = list(attribute)
            new_set = list()
            for i in range(pre_length):
                temp = list()
                value = minus_list[i]

                if x > value:
                    temp.append(value + y)
                    if value > y:
                        new_set.append(value - y)
                        temp.append(value - y)

                    if x - value > y:
                        new_set.append(x - value + y)
                        temp.append(x - value + y)
                        temp.append(x - value + y + y)
                    else:
                        new_set.append(y - x + value)
                        temp.append(y - x + value)
                        temp.append(y - x + value + x)

                if y > value:
                    temp.append(value + x)

                    if value > x:
                        new_set.append(value - x)
                        temp.append(value - x)

                    if y - value > x:
                        new_set.append(y - value + x)
                        temp.append(y - value + x)
                        temp.append(y - value + x + x)
                    else:
                        new_set.append(x - y + value)
                        temp.append(x - y + value)
                        temp.append(x - y + value + y)

                print('new_set is ' + str(new_set))

                if z in temp:
                    return True

            attribute = list(filter(lambda x: x not in whole_nums, new_set))
            whole_nums += attribute
            # print('attribute is ' + str(attribute))

            if 0 >= len(attribute):
                break
            else:
                pre_length = len(attribute)

        return False


solution = Solution()
result = solution.canMeasureWater(22003,31237,1)
# result = solution.canMeasureWater(1,1,0)
# result = solution.canMeasureWater(10000,1, 66)
# result = solution.canMeasureWater(34,5,6)
print('END')
print(result)