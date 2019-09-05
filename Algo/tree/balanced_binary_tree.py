"""

110. Balanced Binary Tree (Easy)

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.




"""

from collections import namedtuple

Result = namedtuple('Result', ('balanced', 'height'))

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.height(root) > 0

    def height(self, node):
        if node is None:
            return 0
        left_height, right_height = self.height(node.left), self.height(node.right)
        if left_height < 0 or right_height < 0 or abs(left_height-right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    def isBalanced2(self, root):
        def dfs(root):
            if not root:
                return Result(True, 0)

            l = dfs(root.left)
            r = dfs(root.right)
            h = max(l.height, r.height)+1

            if not l.balanced or not r.balanced or abs(l.height-r.height) > 1:
                return Result(False, h)
            else:
                return Result(True, h)

        return dfs(root).balanced

