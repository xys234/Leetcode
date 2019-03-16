"""

700. Search in binary search tree

Given the root node of a binary search tree (BST) and a value.
You need to find the node in the BST that the node's value equals the given value.
Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2
     / \
    1   3

In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.



Note that an empty tree is represented by NULL,
therefore you would see the expected output (serialized tree format) as [], not null.

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    def searchBST2(self, root, val):
        """

        :param root:
        :param val:
        :return:

        Recursion
        Space: O(logn)
        Time: O(logn)

        """

        if not root:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST2(root.left, val)
        else:
            return self.searchBST2(root.right, val)


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n7 = TreeNode(7)

    n4.left, n4.right = n2, n7
    n2.left, n2.right = n1, n3
    # n2.left, n2.right = None, n5

    sol = Solution()

    cases = [

        # (sol.numTrees, (3,), 5),
        (sol.searchBST2, (n4, 2), n2),
        (sol.searchBST2, (n4, 5), None),

    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans is expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))