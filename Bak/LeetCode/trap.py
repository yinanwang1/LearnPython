from typing import  List


class Solution:
    def trap(self, height: List[int]) -> int:
        if 2 > len(height):
            return 0

        self.total_drop = 0

        def calc_trap(standard, start, end) -> int:
            print('start is ' + str(start))
            print('end is ' + str(end))
            drop = 0
            for value in height[start: end]:
                drop += standard - value

            print('drop is ' + str(drop))

            return drop

        def left_recursion(index):
            temp_height = height[: index]
            max_height = max(temp_height)
            max_index = temp_height.index(max_height)

            self.total_drop += calc_trap(min(height[index], height[max_index]), max_index, index)

            print('left max_index is ' + str(max_index))

            if max_index > 0:
                left_recursion(max_index)

        def right_recursion(index):
            temp_height = height[index + 1:]
            max_height = max(temp_height)
            max_index = temp_height.index(max_height) + index + 1

            self.total_drop += calc_trap(min(height[index], height[max_index]), index + 1, max_index)

            print('right max_index is ' + str(max_index))

            if max_index != len(height) - 1:
                right_recursion(max_index)

        max_height = max(height)
        max_index = height.index(max_height)
        if max_index > 0:
            left_recursion(max_index)
        if max_index != len(height) - 1:
            right_recursion(max_index)

        return self.total_drop



solution = Solution()
result = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
# result = solution.trap([2,0,2])
print('END')
print(result)