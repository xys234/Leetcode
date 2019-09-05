"""
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

Review: 2019/02/06   Use two queues to achieve level-order

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        levels = []
        q1 = []
        q2 = []

        q1.append(root)
        while q1 or q2:
            level = []
            while q1:
                node = q1.pop(0)
                level.append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            levels.append(level)
            level = []
            while q2:
                node = q2.pop(0)
                level.append(node.val)
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
            if level:
                levels.append(level)

        return levels

    def levelOrder2(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []

        q1, q2 = [root], []
        res = []
        while q1 or q2:
            vals = []
            while q1:
                node = q1.pop(0)
                vals.append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            if vals:
                res.append(vals)

            vals = []
            while q2:
                node = q2.pop(0)
                vals.append(node.val)
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
            if vals:
                res.append(vals)
        return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()
    print(sol.levelOrder2(root))