# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import List


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if tree is None:
            return []

        result = list()
        nodeList = list()
        nodeList.append(tree)

        while len(nodeList) > 0:
            treeListTemp = list()
            listNode = None
            for node in nodeList:
                if listNode is None:
                    listNode = ListNode(node.val)
                    result.append(listNode)
                else:
                    listNode.next = ListNode(node.val)
                    listNode = listNode.next

                if node.left is not None:
                    treeListTemp.append(node.left)
                if node.right is not None:
                    treeListTemp.append(node.right)

            nodeList = treeListTemp

        return result

