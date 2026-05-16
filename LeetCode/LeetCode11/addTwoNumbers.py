from typing import Optional


# 2. 两数相加
# https://leetcode.cn/problems/add-two-numbers/description/



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, left, right = l1, l1, l2
        extra = 0
        while True:
            if left is not None and right is not None:
                value = left.val + right.val + extra
                left.val = value % 10
                extra = value // 10
                if left.next is None and right.next is None:
                    if extra > 0:
                        left.next = ListNode(extra)
                        break
                    else:
                        break
                left_temp = left.next
                right_temp = right.next
                if left_temp is None:
                    left.next = right_temp
                    left = right_temp
                    right = None
                else:
                    left = left_temp
                    right = right_temp
            elif left is not None:
                value = left.val + extra
                left.val = value % 10
                extra = value // 10
                if left.next is None:
                    if extra > 0:
                        left.next = ListNode(extra)
                        break
                    else:
                        break
                else:
                    left = left.next

        return head

