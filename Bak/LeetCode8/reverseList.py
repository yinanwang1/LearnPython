
# 给定单链表的头节点 head ，请反转链表，并返回反转后的链表的头节点。


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        result = None
        while head is not None:
            node = head.next
            head.next = result
            result = head
            head = node

        return result

