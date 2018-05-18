"""

226. Invert Binary Tree (Easy)

Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode

        use pre-order traversal
        """
        if root is None:
            return None

        stack = []
        stack.append(root)
        while stack:
            node = stack.pop(-1)
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root


    def invertTree2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode

        use level order traversal
        """
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

    def peek(self, stack):
        if stack:
            return stack[-1]
        return None

    def post_order_traversal(self, r):
        '''

        :param r:
        :return:
        '''
        res = []
        # Check for empty tree
        if r is None:
            return
        stack = []
        while (True):
            while (r):
                # Push root's right child and then root to stack
                if r.right is not None:
                    stack.append(r.right)
                stack.append(r)
                # Set root as root's left child
                r = r.left

            # Pop an item from stack and set it as root
            r = stack.pop(-1)

            # If the popped item has a right child and the
            # right child is not processed yet, then make sure
            # right child is processed before root
            if r.right is not None and self.peek(stack) == r.right:
                stack.pop(-1)  # Remove right child from stack
                stack.append(r)  # Push root back to stack
                r = r.right  # change root so that the right child is processed next

            # Else print root's data and set root as None
            else:
                res.append(r.val)
                r = None
            if len(stack) <= 0:
                break
        return res

    def post_order_traversal2(self, r):
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
            r = stack.pop(-1)           # visit the root node
            res.append(r.val)
            if r.right:
                stack.append(r.right)   # visit right right-subtree later
            if r.left:
                stack.append(r.left)    # FILO. visit left-subtree first
            if len(stack) == 0:
                break
        return res

if __name__ == "__main__":

    sol = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n9 = TreeNode(9)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n5.left = n8
    n5.right = n9

    print(sol.post_order_traversal(n1))
    print(sol.post_order_traversal2(n1))
    print(sol.in_order_traversal(n1))
    print(sol.pre_order_traversal(n1))
    print(sol.pre_order_traversal(sol.invertTree(n1)))
    print(sol.pre_order_traversal(sol.invertTree2(n1)))


