# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l, r = headA, headB
        while l != r:
            l = l.next if l.next else headB
            r = r.next if r.next else headA

        return l
