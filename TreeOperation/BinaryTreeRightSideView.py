# coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        L = []
        q = deque([])
        if root is not None:
            q.append(root)
        while(q):
            levelSize = len(q)
            l = []
            for i in range(0, levelSize):
                root = q.popleft()
                l.append(root.val)
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
            L.append(l[-1])
        return L