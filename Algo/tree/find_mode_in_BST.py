"""

501. Find Mode in Binary Search Tree

Given a binary search tree (BST) with duplicates, find all the mode(s)
(the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space?
(Assume that the implicit stack space incurred due to recursion does not count).

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def get_num(self, root, value):
        if not root:
            return [[value], 0]
        left = self.get_num(root.left, value)[1]
        right = self.get_num(root.right, value)[1]
        if root.val == value:
            return [[value], left+right+1]
        else:
            return [[value], left+right]

    def traverse(self, root):
        if root:
            cur = self.get_num(root, root.val)
            left = self.traverse(root.left) if root.left else [[0], 0]          # find the mode in left
            right = self.traverse(root.right) if root.right else [[0], 0]       # find the mode in right

            # combine mode for root, left, and right
            if cur[1] < left[1]:
                cur = left
            elif cur[1] == left[1]:
                cur[0] += left[0]
            if cur[1] < right[1]:
                cur = right
            elif cur[1] == right[1]:
                cur[0] += right[0]
            return cur

    def findMode(self, root):
        """

        Time: O(n)
        Space: O(1)

        Actual runtime is much slower than dfs

        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.traverse(root)[0]

    def findMode_dfs(self, root):
        """

        Time: O(n)
        Space: O(n)

        :param root:
        :return:

        use dfs

        """

        if not root:
            return []

        nodes = {}
        def dfs(root: TreeNode):
            if not root:
                return
            if root.left:
                dfs(root.left)
            if root.val in nodes:
                nodes[root.val] +=1
            else:
                nodes[root.val] = 1
            if root.right:
                dfs(root.right)

        dfs(root)
        modes, count = [], 0
        for k, v in nodes.items():
            if v == count:
                modes.append(k)
            if v > count:
                modes.clear()
                modes.append(k)
                count = v
        return modes


if __name__=='__main__':

    sol = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n4 = TreeNode(0)
    n5 = TreeNode(0)
    n6 = TreeNode(2147483647)

    n1.left, n1.right = n4, n2
    n2.left = n3
    n4.left = n5

    print(sol.findMode(n1))
    # print(sol.findMode(n6))