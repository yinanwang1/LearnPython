from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        r_row = 0
        r_column = 0

        for index, row in enumerate(board):
            try:
                r_column = row.index('R')
                r_row = index
                break
            except ValueError:
                continue

        pawn_count = 0
        index = r_row - 1
        while index >= 0:
            value = board[index][r_column]
            if value == '.':
                index -= 1
                continue

            if value == 'B':
                break

            if value == 'p':
                pawn_count += 1
                break

        index = r_row + 1
        while index < 8:
            value = board[index][r_column]
            if value == '.':
                index -= 1
                continue

            if value == 'B':
                break

            if value == 'p':
                pawn_count += 1
                break

        index = r_column - 1
        while index >= 0:
            value = board[r_row][index]
            if value == '.':
                index -= 1
                continue

            if value == 'B':
                break

            if value == 'p':
                pawn_count += 1
                break

        index = r_column + 1
        while index < 8:
            value = board[r_row][index]
            if value == '.':
                index -= 1
                continue

            if value == 'B':
                break

            if value == 'p':
                pawn_count += 1
                break

        return pawn_count






