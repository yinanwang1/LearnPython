# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        使用双指针法
        :param headA:
        :param headB:
        :return:
        '''

        currentA = headA
        currentB = headB

        if currentA is None or currentB is None:
            return None

        while currentA != currentB:
            currentA = currentA.next if currentA is not None else headB
            currentB = currentB.next if currentB is not None else headA

        return currentA



        # listA = list()
        # currentA = headA
        # while currentA is not None:
        #     listA.append(currentA)
        #
        #     currentA = currentA.next
        #
        # listB = list()
        # currentB = headB
        # while currentB is not None:
        #     listB.append(currentB)
        #
        #     currentB = currentB.next
        #
        # listA.reverse()
        # listB.reverse()
        #
        # for i in range(min(len(listA), len(listB))):
        #     if listA[i] != listB[i]:
        #         if i > 0:
        #             return listA[i - 1]
        #         else:
        #             return None
        #
        # return headA if len(listA) < len(listB) else headB
