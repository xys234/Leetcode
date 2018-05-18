"""

105. Construct Binary Tree from Preorder and Inorder Traversal (Medium)

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def in_order_traversal(self, r):
        res = []
        if r is None:
            return None
        stack = []
        while True:
            while r:
                stack.append(r)
                r = r.left
            if r is None and stack:     # reached the end of the left subtree and unvisited nodes present
                top = stack.pop(-1)     # visit the root node
                res.append(top.val)     # visit the root node
                r = top.right           # visit the right subtree

            if len(stack) == 0 and r is None:
                break
        return res

    def pre_order_traversal(self, r):
        res = []
        if r is None:
            return None
        stack = [r]
        while True:
            r = stack.pop(-1)  # visit the root node
            res.append(r.val)
            if r.right:
                stack.append(r.right)  # visit right right-subtree later
            if r.left:
                stack.append(r.left)  # FILO. visit left-subtree first
            if len(stack) == 0:
                break
        return res

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if len(preorder) == 0 or len(inorder)==0:
            return None
        val = preorder.pop(0)
        node = TreeNode(val)
        if len(inorder) > 1:
            ind = inorder.index(val)
            left = inorder[0:ind]
            right = inorder[ind+1:len(inorder)]
            ltree = self.buildTree(preorder,left)
            rtree = self.buildTree(preorder,right)
            node.left = ltree
            node.right = rtree
        return node

if __name__ == "__main__":

    sol = Solution()
    preorder = [1,2,4,5,8,9,3,6,7]
    inorder = [4,2,8,5,9,1,6,3,7]

    tree = sol.buildTree(preorder, inorder)
    print(sol.in_order_traversal(tree))
    print(sol.pre_order_traversal(tree))
