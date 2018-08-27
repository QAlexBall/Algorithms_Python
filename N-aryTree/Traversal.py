class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        res.append(root.val)
        for child in root.children:
            res.extend(self.preorder(child))
        return res

    def preorderWithStack(self, root):
        res = []
        stack = [root]
        if not root:
            return res
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                for i in node.children[::-1]:  # children列表逆序进栈
                    stack.append(i)
        return res

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res

    def levelOrder(self, root):
        """
        :param root:
        :type root: Node
        :return: List[List[int]] res
        """
        res = []
        queue = [root]
        while queue:
            levelSize = len(queue)
            levelList = []
            for i in range(0, levelSize):
                root = queue.pop(0)
                levelList.append(root.val)
                queue.extend(root.children)
            res.append(levelList)
        return res








