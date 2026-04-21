from typing import List


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # 0为墙，1为机器人，2为墙和机器人
        line_map = {}
        for i, r in enumerate(robots):
            line_map[r] = (1, distance[i])
        for v in walls:
            position = line_map.get(v, None)
            if position is None:
                line_map[v] = (0,)
            else:
                line_map[v] = (2, position[1])
        position_destroyed_total = (0, 0)
        right_destroyed_position_list = []
        position_list = sorted(line_map.keys())
        position_list_length = len(position_list)
        for i, r in enumerate(position_list):
            position = line_map[r]
            position_destroyed_total_temp = (0, 0)
            left_destroyed_position_list_temp = []
            right_destroyed_position_list_temp = []
            if 0 == position[0]:
                continue
            if 2 == position[0]:
                position_destroyed_total_temp = (1, 1)

            left, right, current_distance = i - 1, i + 1, position[1]

            while True:
                if left >= 0:
                    # 向左边找
                    left_position = position_list[left]
                    left_line_map_value = line_map[left_position]
                    if 0 == left_line_map_value[0] and r - current_distance <= left_position:
                        position_destroyed_total_temp = (position_destroyed_total_temp[0] + 1,
                                                         position_destroyed_total_temp[1])
                        left_destroyed_position_list_temp.append(left_position)
                        left -= 1
                    else:
                        left = -1

                if right < position_list_length:
                    # 向右边找
                    right_position = position_list[right]
                    right_line_map_value = line_map[right_position]
                    if 0 == right_line_map_value[0] and r + current_distance >= right_position:
                        position_destroyed_total_temp = (position_destroyed_total_temp[0],
                                                         position_destroyed_total_temp[1] + 1)
                        right_destroyed_position_list_temp.append(right_position)
                        right += 1
                    else:
                        right = position_list_length

                if left < 0 and right >= position_list_length:
                    # 向左
                    common = [x for x in right_destroyed_position_list if x in left_destroyed_position_list_temp]
                    left_max = max(position_destroyed_total[0], position_destroyed_total[1] - len(common)) + \
                               position_destroyed_total_temp[0]
                    # 向右
                    right_max = max(position_destroyed_total[0], position_destroyed_total[1]) + \
                                position_destroyed_total_temp[1]

                    right_destroyed_position_list = right_destroyed_position_list_temp
                    position_destroyed_total = (left_max, right_max)
                    break

        return max(position_destroyed_total[0], position_destroyed_total[1])


if __name__ == '__main__':
    # robots = [10,2]
    # distance = [5,1]
    # walls = [5,2,7]
    robots = [17, 59, 32, 11, 72, 18]
    distance = [5, 7, 6, 5, 2, 10]
    walls = [17, 25, 33, 29, 54, 53, 18, 35, 39, 37, 20, 14, 34, 13, 16, 58, 22, 51, 56, 27, 10, 15, 12, 23, 45, 43, 21,
             2, 42, 7, 32, 40, 8, 9, 1, 5, 55, 30, 38, 4, 3, 31, 36, 41, 57, 28, 11, 49, 26, 19, 50, 52, 6, 47, 46, 44,
             24, 48]
    print(Solution().maxWalls(robots, distance, walls))
