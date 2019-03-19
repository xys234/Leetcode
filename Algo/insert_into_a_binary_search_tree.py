"""

701

Given the root node of a binary search tree (BST) and a value to be inserted into the tree,
insert the value into the BST. Return the root node of the BST after the insertion.
It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \
    1   3
         \
          4


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """

        :param root:
        :param val:
        :return:

        Time: O(logn)
        Space: O(logn)

        """

        if not root:
            return TreeNode(val)
        node = root
        while node:
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    return root
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    return root

    def insertIntoBST_recursive(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST_recursive(root.left, val)
        else:
            root.right = self.insertIntoBST_recursive(root.right, val)
        return root


def inorder(root: 'TreeNode', seq: 'list'):
    if not root:
        return
    inorder(root.left, seq)
    seq.append(root.val)
    inorder(root.right, seq)


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

        # (sol.insertIntoBST, (n4, 5), [0, 1, 2, 3, 4, 5, 7]),

        (sol.insertIntoBST_recursive, (n4, 0), [0, 1, 2, 3, 4, 7]),
        (sol.insertIntoBST_recursive, (n4, 5), [0, 1, 2, 3, 4, 5, 7]),

    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        inorder_seq = []
        inorder(ans, inorder_seq)
        if inorder_seq == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(inorder_seq)))