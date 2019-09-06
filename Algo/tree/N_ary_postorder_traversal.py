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
    def postorder_binary(self, root: 'Node'):
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

    def postorder(self, root: 'Node'):
        """

        :param root:
        :return:

        Two stacks approach

        """
        stack, seq = [root], []
        while stack:
            top = stack.pop(-1)
            if top.children:
                stack.extend(top.children)
            seq.append(top.val)
        return list(reversed(seq))


    def postorder_recursive(self, root):
        def traversal(root, ans):
            if root:
                for child in root.children:
                    traversal(child, ans)
                ans.append(root.val)

        res = []
        traversal(root, res)
        return res


if __name__=='__main__':

    sol = Solution()

    n1 = Node(1, None)
    n2 = Node(2, None)
    n3 = Node(3, None)
    n4 = Node(4, None)
    n5 = Node(5, None)
    n6 = Node(6, None)
    n7 = Node(7, None)

    n3.children = [n5, n6]
    n1.children = [n2, n3, n4]


    cases = [

        # (sol.postorder, (3,), 5),
        (sol.postorder, (n1,), [2, 5, 6, 3, 4, 1]),

             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i+1, str(expected), str(ans)))
