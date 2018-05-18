"""

107. Binary Tree Level Order Traversal II (Easy)

Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        stack = list()
        if root:
            stack.append([root])
            top = stack[-1]
        else:
            return []
        while len(top) > 0:
            level = list()
            for n in top:
                if n.left:
                    level.append(n.left)
                if n.right:
                    level.append(n.right)
            if level:
                stack.append(level)
                top = stack[-1]
            else:
                break
        stack.reverse()
        return [[n.val for n in l] for l in stack]

if __name__ == "__main__":

    sol = Solution()

    n1 = TreeNode(3)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n4 = TreeNode(15)
    n5 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5

    print(sol.levelOrderBottom(n1))

    n1 = None



