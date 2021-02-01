# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = list()

        while head is not None:
            nums.append(head.val)
            head = head.next
        numsTemp = nums.copy()
        nums.reverse()

        return numsTemp == nums
