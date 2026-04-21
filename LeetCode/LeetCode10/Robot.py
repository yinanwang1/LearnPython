from typing import List


class Robot:
    width = 0
    height = 0
    position = [0, 0]
    direction = 1
    # 北 东 南 西
    length = len([0, 1, 2, 3])
    direction_value = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
    direction_desc = {0: "North", 1: "East", 2: "South", 3: "West"}

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def step(self, num: int) -> None:
        numTemp = num % (2 * self.width +  2 * self.height - 4)
        if numTemp == 0 and 0 < num and [0, 0] == self.position:
            self.direction = 2

        while numTemp > 0:
            value = self.direction_value[self.direction]
            position_x = self.position[0] + value[0]
            position_y = self.position[1] + value[1]
            if position_x < 0 or position_x >= self.width or position_y < 0 or position_y >= self.height:
                self.direction = (self.direction + self.length - 1) % self.length
                continue
            self.position = [position_x, position_y]
            numTemp -= 1

    def getPos(self) -> List[int]:
        return self.position

    def getDir(self) -> str:
        return self.direction_desc[self.direction]



if __name__ == '__main__':
    steps = 66392
    print(steps %(2 * 97 + 2 * 98 - 4))
