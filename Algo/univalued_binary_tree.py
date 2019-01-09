"""
967.

A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

Easy


"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        elif root.left is None and root.right is None:
            return True

        elif root.left is None and root.right:
            if root.val == root.right.val and self.isUnivalTree(root.right):
                return True

        elif root.left and root.right is None:
            if root.val == root.left.val and self.isUnivalTree(root.left):
                return True

        else:
            if root.val == root.left.val == root.right.val and \
                self.isUnivalTree(root.left) and self.isUnivalTree(root.right):
                return True
        return False


if __name__ == '__main__':

    # [3,3,3,null,null,2,3]

    n1 = TreeNode(2)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n4 = TreeNode(2)
    n5 = TreeNode(2)
    n6 = TreeNode(5)

    n1.left, n1.right = n2, n3
    # n2.left, n2.right = n6, n4
    n3.left, n3.right = n6, n4

    sol = Solution()
    print(sol.isUnivalTree(n1))