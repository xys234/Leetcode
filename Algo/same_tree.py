"""
100. Same Tree (Easy)

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.


Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isSameTree(self, p, q):
        """
        Iterative solution
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p is None and q is None:
            return True
        elif p is not None and q is None:
            return False
        elif q is not None and p is None:
            return False


        s1 = []
        s2 = []

        s1.append(p)
        s2.append(q)


        while s1 and s2:
            n1 = s1.pop(-1)
            n2 = s2.pop(-1)
            if n1.val != n2.val:
                return False
            if n1.right:
                s1.append(n1.right)
                if n2.right is None:
                    return False
            if n2.right:
                s2.append(n2.right)
                if n1.right is None:
                    return False
            if n1.left:
                s1.append(n1.left)
                if n2.left is None:
                    return False
            if n2.left:
                s2.append(n2.left)
                if n1.left is None:
                    return False
            if len(s1) != len(s2):
                return False
        return True

    def isSameTree2(self, p, q):
        """
        Recursive implementation
        :param p:
        :param q:
        :return:
        """

        if p is None and q is None:
            return True
        elif p and q is None or (p is None and q) or (p.val != q.val):
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



if __name__ == "__main__":

    sol = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3

    n4 = TreeNode(1)
    n5 = TreeNode(2)
    n6 = TreeNode(3)
    n4.left = n5
    n4.right = n6

    # print(sol.isSameTree(n1, n4))
    print(sol.isSameTree2(n1, n4))
