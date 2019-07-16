"""

938.

Easy

Given the root node of a binary search tree, return the sum of values of all nodes
with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.



Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23


Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.

"""

from Algo.utilities.tree import *


class Solution:

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        res = 0
        if L <= root.val <= R:
            res += root.val
        if root.val < R:
            res += self.rangeSumBST(root.right, L, R)
        if root.val > L:
            res += self.rangeSumBST(root.left, L, R)
        return res


if __name__ == "__main__":
    sol = Solution()
    method = sol.rangeSumBST

    tree1 = deserialize('[10,5,15,3,7,null,18]')
    # tree2 = deserialize('[5,3,6,2,4,null,null,1]')

    cases = [
        (method, (tree1, 7, 15), 32),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))
