from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if 0 >= len(board):
            return

        board_copy = list()
        for row in board:
            board_copy.append(row.copy())

        rows = len(board_copy)
        columns = len(board_copy[0])
        for row in range(rows):
            for column in range(columns):
                live_nums = 0
                seats = [(row - 1, column - 1), (row, column - 1), (row + 1, column - 1), (row + 1, column),
                         (row + 1, column + 1), (row, column + 1), (row - 1, column + 1), (row - 1, column)]

                for x, y in seats:
                    if 0 <= x < rows and 0 <= y < columns:
                        if 1 == board_copy[x][y]:
                            live_nums += 1

                if 1 == board_copy[row][column]:
                    if 2 <= live_nums <= 3:
                        board[row][column] = 1
                    else:
                        board[row][column] = 0
                else:
                    if live_nums == 3:
                        board[row][column] = 1
                    else:
                        board[row][column] = 0

        return