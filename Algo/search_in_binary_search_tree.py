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

        pass

    def binary_search(self, root, val):
        pass

    def to_array(self, root):
        """
        Do level order traversal and save values to an array
        :param root:
        :return:
        """

        res = []
        queue = []
        queue.append(root)
        while queue:
            ptr = queue.pop(0)
            if ptr:
                res.append(ptr.val)
                queue.append(ptr.left)
                queue.append(ptr.right)
            else:
                res.append(ptr)
        return res


if __name__ == '__main__':
    n1 = TreeNode(4)
    n2 = TreeNode(2)
    n3 = TreeNode(7)
    n4 = TreeNode(1)
    n5 = TreeNode(3)
    n6 = TreeNode(5)

    n1.left, n1.right = n2, n3
    # n2.left, n2.right = n6, n4
    n2.left, n2.right = None, n5

    sol = Solution()
    print(sol.to_array(n1))