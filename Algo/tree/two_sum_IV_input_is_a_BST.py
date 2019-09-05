"""
653. Two Sum IV - Input is a BST (Easy)

Given a Binary Search Tree and a target number,
return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False


Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            node2 = root
            while node2:
                if k - node.val > node2.val:
                    node2 = node2.right
                else:
                    node2 = node2.left
                if node2:
                    if node.val + node2.val == k and node.val != node2.val:
                            return True
        return False

    def findTarget2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        class BSTIterator(object):
            def __init__(self, root, forward):
                self.__node = root
                self.__forward = forward
                self.__s = []
                self.__cur = None
                self.next()

            def val(self):
                return self.__cur

            def next(self):
                while self.__node or self.__s:
                    if self.__node:
                        self.__s.append(self.__node)
                        self.__node = self.__node.left if self.__forward else self.__node.right
                    else:
                        self.__node = self.__s.pop()
                        self.__cur = self.__node.val
                        self.__node = self.__node.right if self.__forward else self.__node.left
                        break

        if not root:
            return False
        left, right = BSTIterator(root, True), BSTIterator(root, False)
        while left.val() < right.val():
            if left.val() + right.val() == k:
                return True
            elif left.val() + right.val() < k:
                left.next()
            else:
                right.next()
        return False


if __name__ == "__main__":
    sol = Solution()

    n1 = TreeNode(5)
    n2 = TreeNode(3)
    n3 = TreeNode(6)
    n4 = TreeNode(2)
    n5 = TreeNode(4)
    n6 = TreeNode(9)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n6

    #print(sol.findTarget2(n1, 9))
    print(sol.findTarget2(n1, 10))
    print(sol.findTarget2(n1, 16))
    print(sol.findTarget(n1, -1))