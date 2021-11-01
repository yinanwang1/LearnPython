class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        nameIndex = 0
        typedIndex = 0
        while True:
            if typedIndex >= len(typed):
                break

            if nameIndex >= len(name):
                nameIndex = len(name) - 1

            if name[nameIndex] == typed[typedIndex]:
                nameIndex += 1
                typedIndex += 1
                continue

            if nameIndex - 1 >= 0 and name[nameIndex - 1] == typed[typedIndex]:
                typedIndex += 1
            else:
                break

        return len(name) == nameIndex