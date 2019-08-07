"""

1028.

Hard

We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node),
then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.
The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.

Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

"""

import string
from Algo.utilities.tree import *


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        num, pos = self.read_value(S, 0, -1)
        root = TreeNode(num)
        self.build(S, 0, pos, root)
        return root

    def build(self, S, depth, pos, root):
        """

        :param S:
        :param depth: current depth
        :param pos:
        :param root:
        :return:
        """
        num, pos = self.read_value(S, depth+1, pos)
        if num > 0:
            root.left = TreeNode(num)
            self.build(S, depth+1, pos, root.left)
        else:
            num, pos = self.read_value(S, depth, pos)
            root.right = TreeNode(num)
            self.build(S, depth + 1, pos, root.right)

    def read_value(self, S, depth, pos):
        """

        Return the next value given depth and current position in S

        :param S:
        :param depth:
        :param pos:
        :return:
        """
        start = pos+depth+1
        if start >= len(S) or S[start] not in string.digits:
            return -1, pos
        else:
            end = start + 1
            while end < len(S) and S[end] in string.digits:
                end += 1
            return int(S[start:end]), end-1

    def recoverFromPreorder_solution(self, S: str) -> TreeNode:
        # recover by pre-order
        # parse nodes' info
        info = []
        i, j = 0, 0
        n = len(S)
        digits = set(string.digits)

        while i < len(S):
            while S[i] == '-':
                i += 1
            depth = i - j
            j = i

            while j < n and S[j] in digits:
                j += 1
            j = min(j, n)
            info.append((depth, S[i:j]))
            i = j

        self.has_built = 0      # has built x nodes

        def preorder(depth):
            if self.has_built >= len(info) or info[self.has_built][0] != depth:
                return None
            node = TreeNode(info[self.has_built][1])
            self.has_built += 1
            node.left = preorder(depth+1)
            node.right = preorder(depth+1)
            return node

        return preorder(0)


if __name__ == '__main__':
    sol = Solution()
    method = sol.recoverFromPreorder_solution

    cases = [

        (method, ("1-2--3--4-5--6--7",), [1,2,3,4,5,6,7]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        ans = preorder(ans)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))

    # S = "177-233--38943--4-5--6--7"
    # S = "1-2--3--4-5--6--7"
    # depth = 0
    # val, pos = sol.read_value(S, depth, -1)
    # print(val, pos)
    # val, pos = sol.read_value(S, depth+1, pos)
    # print(val, pos)