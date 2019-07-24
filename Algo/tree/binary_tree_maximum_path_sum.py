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
        self.maxi = root.val

        def dfs(node):
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            m = max(l, 0) + node.val + max(r, 0)
            self.maxi = max(m, self.maxi)
            ret = max(node.val + l, node.val + r, node.val)
            return ret
        dfs(root)
        return self.maxi


if __name__ == "__main__":
    sol = Solution()
    method = sol.maxPathSum

    tree1 = deserialize('[1,2,3]')
    tree2 = deserialize('[-10,9,20,null,null,15,7]')
    tree3 = deserialize('[-2,null,-3]')
    tree4 = deserialize('[1,-2,-3,1,3,-2,null,-1]')
    tree5 = deserialize('[5,4,8,11,null,13,4,7,2,null,null,null,1]')
    tree6 = deserialize('[-2,-1,-3]')

    cases = [
        (method, (tree1, ), 6),
        (method, (tree2, ), 42),
        (method, (tree3, ), -2),
        (method, (tree4, ), 3),
        (method, (tree5, ), 48),
        (method, (tree6, ), -1),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))