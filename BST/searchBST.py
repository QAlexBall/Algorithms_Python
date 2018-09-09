"""
给定二叉搜索树（BST）的根节点和一个值。
你在BST中找到节点值等于给定值的节点。
返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
"""
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
