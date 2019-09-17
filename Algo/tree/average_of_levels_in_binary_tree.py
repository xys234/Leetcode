"""



"""
from typing import List
from Algo.utilities.tree import *


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        levels = self.level_order_traversal(root)
        print(levels)
        return [sum(l) / len(l) for l in levels]

    def level_order_traversal(self, root):
        q1, q2 = [root], []
        levels = []
        while q1 or q2:
            level = []
            while q1:
                node = q1.pop(0)
                level.append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            if level:
                levels.append(level[:])

            level.clear()
            while q2:
                node = q2.pop(0)
                level.append(node.val)
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
            if level:
                levels.append(level[:])
            level.clear()
        return levels


if __name__ == "__main__":
    sol = Solution()
    method = sol.averageOfLevels

    tree1 = deserialize('[3,9,20,null,null,15,7]')
    # tree2 = deserialize('[10,8,null,2]')
    # tree3 = deserialize('[10,2,null,-2]')

    cases = [
        (method, (tree1, ), [3, 14.5, 11]),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))