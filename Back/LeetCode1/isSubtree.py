# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        tNodeList = list()

        nodeList = [s]
        while len(nodeList) > 0:
            nodeListTemp = list()

            for node in nodeList:
                if node.val == t.val:
                    tNodeList.append(node)
                if node.left is not None:
                    nodeListTemp.append(node.left)
                if node.right is not None:
                    nodeListTemp.append(node.right)

            nodeList = nodeListTemp

        if len(tNodeList) <= 0:
            return False

        def isSame(node1: TreeNode, node2: TreeNode) -> bool:
            node1List = [node1]
            node2List = [node2]

            while len(node1List) > 0 or len(node2List) > 0:
                node1ListTemp = list()
                node2ListTemp = list()

                if len(node1List) != len(node2List):
                    return False

                for index in range(len(node1List)):
                    node1Temp = node1List[index]
                    node2Temp = node2List[index]
                    if node1Temp.val != node2Temp.val:
                        return False

                    if node1Temp.left is not None:
                        if node2Temp.left is None:
                            return False
                        else:
                            if node1Temp.left.val != node2Temp.left.val:
                                return False

                            node1ListTemp.append(node1Temp.left)
                            node2ListTemp.append(node2Temp.left)
                    else:
                        if node2Temp.left is not None:
                            return False

                    if node1Temp.right is not None:
                        if node2Temp.right is None:
                            return False
                        else:
                            if node1Temp.right.val != node2Temp.right.val:
                                return False

                            node1ListTemp.append(node1Temp.right)
                            node2ListTemp.append(node2Temp.right)
                    else:
                        if node2Temp.right is not None:
                            return False

                node1List = node1ListTemp
                node2List = node2ListTemp

            return True

        result = False

        for node in tNodeList:
            result = isSame(node, t)
            if result:
                return True

        return result

