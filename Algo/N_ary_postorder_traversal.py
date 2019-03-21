"""



"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.val})"

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

    def __repr__(self):
        return f"Node({self.val})"


class Solution:
    def postorder(self, root: 'Node'):
        stack, seq = [root], []
        while stack:
            top = stack[-1]
            if top.left:
                stack.append(top.left)
                top.left = None
            elif top.right:
                stack.append(top.right)
                top.right = None
            else:
                seq.append(top.val)
                stack.pop(-1)
        return seq


if __name__=='__main__':

    sol = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.right = n7

    cases = [

        # (sol.postorder, (3,), 5),
        (sol.postorder, (n1,), [4, 5, 2, 7, 3, 1]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))
