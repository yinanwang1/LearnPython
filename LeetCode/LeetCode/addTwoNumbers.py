from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def nodeToValue(node: ListNode) -> int:
            result = 0

            while node is not None:
                result = result * 10 + node.val

                node = node.next

            return result

        value = list(str(nodeToValue(l1) + nodeToValue(l2)))
        value.reverse()

        current = ListNode(value[0])
        value.pop(0)

        for num in value:
            node = ListNode(num)
            node.next = current

            current = node

        return current





