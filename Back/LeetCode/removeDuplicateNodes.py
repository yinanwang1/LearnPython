# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        values = list()
        current = head
        pre_node = None

        while current is not None:
            if current.val in values:
                if current.next is None:
                    current = None
                    if pre_node is not None:
                        pre_node.next = None
                else:
                    current.val = current.next.val
                    current.next = current.next.next
            else:
                values.append(current.val)

                pre_node = current
                current = current.next

        return head