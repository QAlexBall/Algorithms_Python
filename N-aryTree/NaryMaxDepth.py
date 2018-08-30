class Solution(object):
    def maxDepth(self, root):
        depth = 0;
        if root is None:
            return 0
        if root.children is None:
            return 1
        depth = max(self.maxDepth(child) for child in root.children) + 1
        return depth