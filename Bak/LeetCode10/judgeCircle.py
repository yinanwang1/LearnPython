
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        left, right, upper, down = 'L', 'R', 'U', 'D'
        x, y = 0, 0
        for move in moves:
            if move == left:
                x -= 1
            elif move == right:
                x += 1
            elif move == upper:
                y -= 1
            elif move == down:
                y += 1
        return x == 0 and y == 0

