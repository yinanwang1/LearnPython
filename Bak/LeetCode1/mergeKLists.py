from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        resultFirst = ListNode(0)
        result = resultFirst

        lists = list(filter(lambda x: x is not None, lists))

        while 0 < len(lists):
            minNode = min(lists, key=lambda x: x.val)
            result.next = ListNode(minNode.val)
            result = result.next

            lists.remove(minNode)
            if minNode.next is not None:
                lists.append(minNode.next)

        return resultFirst.next