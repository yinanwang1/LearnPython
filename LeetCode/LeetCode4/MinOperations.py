from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = list()

        for log in logs:
            if log == "../":
                if len(result) > 0:
                    result.pop()
            elif log == "./":
                pass
            else:
                result.append(log)

        return len(result)
