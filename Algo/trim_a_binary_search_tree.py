"""

669. Trim a Binary Search Tree (Easy)

Given a binary search tree and the lowest and highest boundaries as L and R,
trim the tree so that all its elements lies in [L, R] (R >= L).
You might need to change the root of the tree,
so the result should return the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        r = root
        if r:
            if r.val < L:
                r = self.trimBST(r.right, L, R)
            elif r.val > R:
                r = self.trimBST(r.left, L, R)
            else:
                r.left = self.trimBST(r.left, L, R)
                r.right = self.trimBST(r.right, L, R)
            return r

    def pre_order_traversal(self, r):
        res = []
        if r is None:
            return None
        stack = [r]
        while True:
            r = stack.pop(-1)           # visit the root node
            res.append(r.val)
            if r.right:
                stack.append(r.right)   # visit right right-subtree later
            if r.left:
                stack.append(r.left)    # FILO. visit left-subtree first
            if len(stack) == 0:
                break
        return res

if __name__ == "__main__":

    sol = Solution()

    # n1 = TreeNode(1)
    # n2 = TreeNode(0)
    # n3 = TreeNode(2)
    #
    # n1.left = n2
    # n1.right = n3
    # print(sol.pre_order_traversal(n1))
    # print(sol.pre_order_traversal(sol.trimBST(n1, 1, 2)))

    n1 = TreeNode(3)
    n2 = TreeNode(0)
    n3 = TreeNode(4)
    n4 = TreeNode(2)
    n5 = TreeNode(1)

    n1.left = n2
    n1.right = n3
    n2.right = n4
    n4.left = n5

    print(sol.pre_order_traversal(n1))
    print(sol.pre_order_traversal(sol.trimBST(n1, 1, 3)))