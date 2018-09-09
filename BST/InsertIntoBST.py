# coding=utf-8
"""
给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。
返回插入后二叉搜索树的根节点。 保证原始二叉搜索树中不存在新值。
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insertIntoBST(self, root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    if root is None:
        node = TreeNode(val)
        root = node

    if root.val > val:
        if root.left is None:
            node = TreeNode(val)
            root.left = node
        self.insertIntoBST(root.left, val)

    if root.val < val:
        if root.right is None:
            node = TreeNode(val)
            root.right = node
        self.insertIntoBST(root.right, val)
    return root