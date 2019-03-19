"""

108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the
two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: 'list[int]') -> 'TreeNode':
        """

        :param nums:
        :return:
        """

        if not nums:
            return None

        n = len(nums)

        def helper(l, r):
            if l > r or r < l:
                return None
            if l == r:
                return TreeNode(nums[l])
            root_index = int((l+r)/2)
            root = TreeNode(nums[root_index])
            root.left = helper(l, root_index-1)
            root.right = helper(root_index+1, r)
            return root

        return helper(0, n-1)


def inorder(root: 'TreeNode', seq: 'list'):
    if not root:
        return
    inorder(root.left, seq)
    seq.append(root.val)
    inorder(root.right, seq)


if __name__ == '__main__':

    sol = Solution()

    cases = [


        (sol.sortedArrayToBST, ([-10, -3, 0, 5, 9], ), [-10, -3, 0, 5, 9]),
        (sol.sortedArrayToBST, ([-12, -10, -3, 0, 5, 9], ), [-12, -10, -3, 0, 5, 9]),

    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        inorder_seq = []
        inorder(ans, inorder_seq)
        if inorder_seq == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(inorder_seq)))