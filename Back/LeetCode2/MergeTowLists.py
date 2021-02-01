from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        l1Head = l1
        l2Head = l2
        if l2.val < l1.val:
            resultHead = l2
            result = l2
            l2Head = l2Head.next
        else:
            resultHead = l1
            result = l1
            l1Head = l1Head.next

        while True:
            if l1Head is None:
                result.next = l2Head
                break
            if l2Head is None:
                result.next = l1Head
                break

            if l1Head.val < l2Head.val:
                result.next = l1Head
                l1Head = l1Head.next
            else:
                result.next = l2Head
                l2Head = l2Head.next

            result = result.next

        return resultHead

