"""
98.

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if root is None:
            return True

        def dfs(r, lower_bound, upper_bound):
            if r is None:
                return True

            if lower_bound is not None and r.val <= lower_bound:
                return False

            if upper_bound is not None and r.val >= upper_bound:
                return False

            if r.left:
                check_left = dfs(r.left, lower_bound, r.val)
            else:
                check_left = True
            if not check_left:
                return False
            else:
                if r.right:
                    check_right = dfs(r.right, r.val, upper_bound)
                else:
                    check_right = True
                return check_right

        return dfs(root, None, None)

    def isValidBST_solution_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def isBSTHelper(node, lower_limit, upper_limit):
            if lower_limit is not None and node.val <= lower_limit:
                return False
            if upper_limit is not None and upper_limit <= node.val:
                return False

            left = isBSTHelper(node.left, lower_limit, node.val) if node.left else True
            if left:
                right = isBSTHelper(node.right, node.val, upper_limit) if node.right else True
                return right
            else:
                return False

        return isBSTHelper(root, None, None)

    def isValidBST_solution_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [(root, None, None), ]
        while stack:
            root, lower_limit, upper_limit = stack.pop()
            if root.right:
                if root.right.val > root.val:
                    if upper_limit and root.right.val >= upper_limit:
                        return False
                    stack.append((root.right, root.val, upper_limit))
                else:
                    return False
            if root.left:
                if root.left.val < root.val:
                    if lower_limit and root.left.val <= lower_limit:
                        return False
                    stack.append((root.left, lower_limit, root.val))
                else:
                    return False
        return True


if __name__=='__main__':

    sol = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n10 = TreeNode(10)
    n11 = TreeNode(-1)
    n12 = TreeNode(0)
    n15 = TreeNode(15)
    n20 = TreeNode(20)

    # Tree1
    n2.left, n2.right = n1, n3

    # Tree2
    n5.left, n5.right = n1, n4
    n4.left, n4.right = n3, n6

    # Tree3
    n10.left, n10.right = n5, n15
    n15.left, n15.right = n6, n20

    # Tree4
    n12.left, n12.right = None, n11

    cases = [

        (sol.isValidBST, (n2,), True),
        (sol.isValidBST, (n5,), False),
        (sol.isValidBST, (n10,), False),
        (sol.isValidBST, (n12,), False),


             ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != Output {:s}".format(i+1, str(expected), str(ans)))