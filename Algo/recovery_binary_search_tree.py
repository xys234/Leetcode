"""



"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.prev = None
        self.firstNode = None
        self.secondNode = None

    def inorder(self, root):
        if root == None:
            return

        self.inorder(root.left)

        if self.prev and self.prev.val >= root.val and self.firstNode == None:
            self.firstNode = self.prev

        if self.prev and self.prev.val >= root.val and self.firstNode != None:
            self.secondNode = root

        self.prev = root

        self.inorder(root.right)

    def recoverTree(self, root):
        self.inorder(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val


if __name__ == '__main__':

    sol = Solution()

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n1.left = n3
    n3.right = n2

    sol.recoverTree(n1)