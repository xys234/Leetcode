"""

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


"""


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        # empty tree
        if not root:
            return 0

        # leaf node
        if not root.children:
            return 1

        depth = 0
        for child in root.children:
            depth = max(depth, 1 + self.maxDepth(child))
        return depth