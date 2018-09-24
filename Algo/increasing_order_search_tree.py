"""

Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree,
and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9
Note:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST_Slow(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        seq = []
        stack = []
        stack.append(root)
        current = root
        while stack:
            if current:
                if current.left:
                    stack.append(current.left)
                current = current.left
            else:
                current = stack.pop(len(stack)-1)
                seq.append(current.val)
                current = current.right
                if current:
                    stack.append(current)

        res = []
        for i, _ in enumerate(seq):
            if i != len(seq) - 1:
                res.extend([seq[i], None])
            else:
                res.append(seq[i])
        return res

    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = cur = TreeNode(v)
        return ans.right

if __name__=='__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n9 = TreeNode(9)

    n5.left = n3
    n5.right = n6
    n3.left = n2
    n3.right = n4
    n2.left = n1
    n5.right = n6
    n6.right = n8
    n8.left = n7
    n8.right = n9

    sol = Solution()
    print(sol.increasingBST(n5))


























