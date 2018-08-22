import Tree


class Solution(object):

    # inorderTraversal with stack
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                t = stack.pop()
                ret.append(t.val)
                root = t.right
        return ret


root = Tree.TreeNode(1)
root.left = Tree.TreeNode(2)
root.right = Tree.TreeNode(3)
print(Solution().inorderTraversal(root))

input = '1, 2, 3'
root1 = Tree.stringToTreeNode(input)

print(root1)
print(Solution().inorderTraversal(root1))
