# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node_list = [head]
        current = head.next

        while current is not None:
            node_list.append(current)

            current = current.next

        middle = len(node_list) // 2
        if len(node_list) % 2 == 0:
            return node_list[middle + 1]
        else:
            return node_list[middle]