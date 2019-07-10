"""

124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along
the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42


"""

from Algo.utilities.tree import *

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        left, right = -float('inf'), -float('inf')

        if root.left is None and root.right is None:
            return root.val

        elif root.left is not None and root.right is None:
            left = self.maxPathSum(root.left)
            root.left.max = left
            if root.val < 0:
                root.max = max(left, root.val)
            else:
                if root.left.val < 0:
                    root.max = root.val
                else:
                    root.max = left + root.val

        elif root.right is not None and root.left is None:
            right = self.maxPathSum(root.right)
            root.right.max = right
            if root.val < 0:
                root.max = max(right, root.val)
            else:
                if root.right.val < 0:
                    root.max = root.val
                else:
                    root.max = right + root.val
        else:
            left = self.maxPathSum(root.left)
            right = self.maxPathSum(root.right)
            if root.val < 0:
                root.max = max(left, right, root.val)
            else:
                if root.left.val >= 0 and root.right.val >= 0:
                    root.max = left + right + root.val
                elif root.left.val < 0 and root.right.val < 0:
                    root.max = max(left, right, root.val)
                elif root.left.val < 0 <= root.right.val:
                    root.max = max(left, right + root.val)
                else:
                    root.max = max(right, left + root.val)
        return root.max


if __name__ == "__main__":
    sol = Solution()
    method = sol.maxPathSum

    tree1 = deserialize('[1,2,3]')
    tree2 = deserialize('[-10,9,20,null,null,15,7]')
    tree3 = deserialize('[-2,null,-3]')
    tree4 = deserialize('[1,-2,-3,1,3,-2,null,-1]')
    tree5 = deserialize('[5,4,8,11,null,13,4,7,2,null,null,null,1]')

    cases = [
        # (method, (tree1, ), 6),
        # (method, (tree2, ), 42),
        # (method, (tree3, ), -2),
        # (method, (tree4, ), 3),
        (method, (tree5, ), 48),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))