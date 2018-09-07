def searchBST(self, root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    if root is None:
        return None
    if root.val == val:
        return root
    if root.val > val:
        return self.searchBST(root.left, val)
    if root.val < val:
        return self.searchBST(root.right, val)