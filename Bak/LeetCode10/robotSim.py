from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        robot_position, robot_direction = [0, 0], 0
        # 北 东 南 西
        directions = [0, 1, 2, 3]
        length = len(directions)
        direction_value = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
        mp = set([tuple(i) for i in obstacles])
        res = 0
        for command in commands:
            if -2 == command:
                robot_direction = (robot_direction + length - 1) % length
            elif -1 == command:
                robot_direction = (robot_direction + length + 1) % length
            else:
                value = direction_value[robot_direction]
                for step in range(command):
                    position = [robot_position[0] + value[0], robot_position[1] + value[1]]
                    if tuple(position) in mp:
                        break
                    robot_position = position
                res = max(res, robot_position[0] ** 2 + robot_position[1] ** 2)
        return res


if __name__ == '__main__':
    commands = [4,-1,3]
    obstacles =[]
    solution = Solution()
    print(solution.robotSim(commands, obstacles))

