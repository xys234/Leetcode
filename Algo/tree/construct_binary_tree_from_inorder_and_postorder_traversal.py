"""

106. Construct Binary Tree from Inorder and Postorder Traversal (Medium)

Given inorder and postorder traversal of a tree, construct the binary tree.

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

    def post_order_traversal(self, r):
        '''
        Two-stack implementation
        :param r:
        :return:
        '''

        s1 = []
        s2 = []
        res = []
        s1.append(r)
        while s1:
            node = s1.pop(-1)
            s2.append(node)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        while s2:
            res.append((s2.pop(-1)).val)
        return res

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if len(postorder) == 0 or len(inorder) == 0:
            return None
        val = postorder.pop(-1)
        node = TreeNode(val)
        if len(inorder) > 1:
            ind = inorder.index(val)
            left = inorder[0:ind]
            right = inorder[ind+1:len(inorder)]
            rtree = self.buildTree(right, postorder)
            ltree = self.buildTree(left, postorder)
            node.left = ltree
            node.right = rtree
        return node

if __name__ == "__main__":

    sol = Solution()
    postorder = [4,8,9,5,2,6,7,3,1]
    inorder = [4,2,8,5,9,1,6,3,7]

    tree = sol.buildTree(inorder, postorder)
    print(sol.in_order_traversal(tree))
    print(sol.post_order_traversal(tree))

