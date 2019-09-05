"""


"""

from Algo.utilities.tree import *


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        def dfs(node, s):
            """
            number of paths that use the current node
            :param node:
            :param s:
            :return:
            """
            count = 0
            if not node:
                return 0

            if node.val == s:
                count += 1

            count += dfs(node.left, s-node.val)
            count += dfs(node.right, s-node.val)

            return count

        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


if __name__ == "__main__":
    sol = Solution()
    method = sol.pathSum

    tree1 = deserialize('[10,5,-3,3,2,null,11,3,-2,null,1]')
    tree2 = deserialize('[10,8,null,2]')
    tree3 = deserialize('[10,2,null,-2]')

    cases = [
        # (method, (tree1, 8), 3),
        # (method, (tree2, 10), 2),
        (method, (tree3, 10), 2),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))