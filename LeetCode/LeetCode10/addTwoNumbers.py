




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s, t = [], []
        while l1:
            s.append(l1.val)
            l1 = l1.next
        while l2:
            t.append(l2.val)
            l2 = l2.next
        carry = 0
        result = None
        while 0 != len(s) or 0 != len(t) or 0 != carry:
            a = 0 if 0 == len(s) else s.pop()
            b = 0 if 0 == len(t) else t.pop()
            sum_value = a + b + carry
            val = sum_value % 10
            carry = sum_value // 10
            result = ListNode(val, next=result)

        return result




if __name__ == '__main__':
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    solution = Solution()
    res = solution.addTwoNumbers(l1, l2)
    while res is not None:
        print(res.val)
        res = res.next


