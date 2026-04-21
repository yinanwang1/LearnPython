# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        headList = set()
        headList.add(head)
        headTemp = head.next
        while headTemp is not None:
            nums = len(headList)
            headTemp = headTemp.next
            headList.add(headTemp)
            if nums == len(headList):
                return True

        return False


