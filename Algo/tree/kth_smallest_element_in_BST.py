"""
230. Kth Smallest Element in a BST

Medium

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?

Maintain a linked list of k smallest elements. 

Review:
1. 2019-06-21

"""

from Algo.utilities.tree import *


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        top_k = []
        self.inorder(root, top_k, k)
        return top_k[k-1]

    def inorder(self, root, elems, k):
        if not root:
            return
        self.inorder(root.left, elems, k)
        elems.append(root.val)
        if len(elems) == k:
            return
        self.inorder(root.right, elems, k)

    def kthSmallest2(self, root, k):
        arr = []

        def inorder_traversal(r):
            if not r:
                return False

            if inorder_traversal(r.left):
                return True
            arr.append(r.val)
            if len(arr) == k:
                return True
            if inorder_traversal(r.right):
                return True
            return False

        inorder_traversal(root)
        return arr[-1]


if __name__ == "__main__":
    sol = Solution()
    method = sol.kthSmallest2

    tree1 = deserialize('[3,1,4,null,2]')
    tree2 = deserialize('[5,3,6,2,4,null,null,1]')

    cases = [
        (method, (tree1, 1), 1),
        (method, (tree2, 3), 3),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))
