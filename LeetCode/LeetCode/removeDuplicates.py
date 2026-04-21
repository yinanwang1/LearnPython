class Solution:
    def removeDuplicates(self, S: str) -> str:
        index = 0
        string_list = list(S)

        while index + 1 < len(string_list):
            if string_list[index] == string_list[index + 1]:
                string_list.pop(index)
                string_list.pop(index)

                index = (index - 1 if index - 1 >= 0 else 0)
            else:
                index += 1

        return ''.join(string_list)
