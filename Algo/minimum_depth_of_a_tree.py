"""

111. Minimum Depth of Binary Tree (Easy)

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        left_depth, right_depth = self.minDepth(root.left), self.minDepth(root.right)
        if left_depth == 0 and right_depth == 0 or left_depth > 0 and right_depth > 0:
            return min(left_depth, right_depth) + 1
        elif left_depth > 0 and right_depth == 0:
            return left_depth + 1
        else:
            return right_depth + 1