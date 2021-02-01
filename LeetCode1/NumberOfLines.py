from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        length = 0
        for char in s:
            cell = widths[ord(char) - 97]
            if length + cell > 100:
                lines += 1
                length = cell
            else:
                length += cell

        return [lines, length]

