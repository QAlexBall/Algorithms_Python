class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []

        def inOrder(root):
            if not root:
                return
            inOrder(root.right)
            self.stack.append(root.val)
            inOrder(root.left)

        inOrder(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
