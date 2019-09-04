"""
865.

Medium


Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]

2019.7.29

"""

from collections import namedtuple
from Algo.utilities.tree import *


class Solution(object):
    def subtreeWithAllDeepest_solution(self, root):
        # The result of a subtree is:
        # Result.node: the largest depth node that is equal to or
        #              an ancestor of all the deepest nodes of this subtree.
        # Result.dist: the number of nodes in the path from the root
        #              of this subtree, to the deepest node in this subtree.
        Result = namedtuple("Result", ("node", "dist"))

        def dfs(node):
            # Return the result of the subtree at this node.
            if not node: return Result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.dist > R.dist: return Result(L.node, L.dist + 1)
            if L.dist < R.dist: return Result(R.node, R.dist + 1)
            return Result(node, L.dist + 1)

        return dfs(root).node

    def subtreeWithAllDeepest(self, root):

        def height(node):
            if not node:
                return 0

            l = height(node.left)
            r = height(node.right)
            node.height = max(l, r) + 1
            return node.height

        def helper(node):
            if not node:
                return

            left = helper(node.left)
            right = helper(node.right)

            if not left and not right:
                return None
            elif left and not right:
                return left
            elif right and not left:
                return right
            else:
                if node.left.height > node.right.height:
                    return node.left
                elif node.left.height < node.right.height:
                    return node.right
                else:
                    return node

        height(root)
        return helper(root)


if __name__ == "__main__":
            sol = Solution()
            method = sol.subtreeWithAllDeepest

            tree1 = deserialize('[3,1,4,null,2]')
            tree2 = deserialize('[5,3,6,2,4,null,null,1]')

            cases = [
                (method, (tree1,), 2),
                (method, (tree2,), 3),
            ]

            for i, (func, case, expected) in enumerate(cases):
                ans = func(*case)
                if ans == expected:
                    print("Case {:d} Passed".format(i + 1))
                else:
                    print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))