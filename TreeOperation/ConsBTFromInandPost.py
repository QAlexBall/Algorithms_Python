from TreeOperation import Tree


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inStart = 0
        inEnd = len(inorder) - 1
        postEnd = len(postorder) - 1
        return self.build(inorder, postorder, inStart, inEnd, postEnd)

    def build(self, inorder, postorder, inStart, inEnd, postEnd):
        if inStart > inEnd or postEnd < 0:
            return None
        root = Tree.TreeNode(postorder[postEnd])

        index = 0
        for i in range(inStart, inEnd + 1):  # 浪费大量时间
            if inorder[i] == root.val:
                index = i
                break

        root.left = self.build(inorder, postorder, inStart, index - 1, postEnd - (inEnd - index) - 1)
        root.right = self.build(inorder, postorder, index + 1, inEnd, postEnd - 1)
        return root

    def buildTree1(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i
        return self.buildTreeRecu(lookup, postorder, inorder, len(postorder), 0, len(inorder))

    def buildTreeRecu(self, lookup, postorder, inorder, post_end, in_start, in_end):
        if in_start == in_end:
            return None
        node = Tree.TreeNode(postorder[post_end - 1])
        i = lookup[postorder[post_end - 1]]
        node.left = self.buildTreeRecu(lookup, postorder, inorder, post_end - 1 - (in_end - i - 1), in_start, i)
        node.right = self.buildTreeRecu(lookup, postorder, inorder, post_end - 1, i + 1, in_end)
        return node

    def buildTreeFromPreAndIn(self, preorder, inorder):
        """
        :param preorder: List[int]
        :param inorder: List[int]
        :return: TreeNode
        """
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i

        def buildTreeRecu(lookup, preorder, inorder, pre_start, in_start, in_end):
            if in_start == in_end:
                return None
            node = Tree.TreeNode(preorder[pre_start])
            i = lookup[preorder[pre_start]]
            node.left = buildTreeRecu(lookup, preorder, inorder, pre_start + 1, in_start, i)
            node.right = buildTreeRecu(lookup, preorder, inorder, pre_start + i - in_start + 1, i + 1, in_end)
            return node

        return buildTreeRecu(lookup, preorder, inorder, 0, 0, len(inorder))


def main():
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    buildBT = Solution()
    root = buildBT.buildTree1(inorder, postorder)
    print(Tree.treeNodeToString(root))


if __name__ == '__main__':
    main()
