# 给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 进阶:
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head1Temp = l1.next
        head1.next = None

        head2 = l2
        head2Temp = l2.next
        head2.next = None

        while head1Temp is not None or head2Temp is not None:
            if head1Temp is not None:
                temp = head1Temp.next
                head1Temp.next = head1
                head1 = head1Temp
                head1Temp = temp

            if head2Temp is not None:
                temp = head2Temp.next
                head2Temp.next = head2
                head2 = head2Temp
                head2Temp = temp

        # head1,head2 指向个位数
        result = None
        external = 0
        while head1 is not None or head2 is not None:
            if head1 is not None and head2 is not None:
                temp = head1.next

                head1.val += head2.val + external
                external = head1.val // 10
                head1.val %= 10

                head1.next = result
                result = head1

                head1 = temp
                head2 = head2.next
            elif head1 is not None:
                temp = head1.next

                head1.val += external
                external = head1.val // 10
                head1.val %= 10

                head1.next = result
                result = head1

                head1 = temp
            elif head2 is not None:
                temp = head2.next

                head2.val += external
                external = head2.val // 10
                head2.val %= 10

                head2.next = result
                result = head2

                head2 = temp

        if external > 0:
            node = ListNode(val=external)
            node.next = result

            result = node

        return result
