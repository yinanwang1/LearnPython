# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        elements = [head.val]
        headTemp = head
        while headTemp.next is not None:
            if headTemp.next.val in elements:
                headTemp.next = headTemp.next.next
            else:
                elements.append(headTemp.next.val)
                headTemp = headTemp.next

        return head


