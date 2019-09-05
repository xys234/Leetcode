"""

173. Binary Search Tree Iterator (Medium)

Implement an iterator over a binary search tree (BST).
Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Your BSTIterator will be called like this:
i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())

"""



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """



    def hasNext(self):
        """
        :rtype: bool
        """

    def next(self):
        """
        :rtype: int
        """

class BSTIterator2(object):
    def __init__(self, root, forward):
        """
        :param root:
        :param forward: next smallest or next biggest
        """

        self.__node = root
        self.__forward = forward
        self.__s = []
        self.__cur = None
        while self.__node:
            self.__cur = self.__node.val
            self.__s.append(self.__node)
            self.__node = self.__node.left if self.__forward else self.__node.right

    def hasNext(self):
        """
        :rtype: bool
        """

        if self.__node or self.__s:
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """

        while self.__node or self.__s:
            if self.__node:
                self.__s.append(self.__node)
                self.__node = self.__node.left if self.__forward else self.__node.right
            else:
                self.__node = self.__s.pop()
                self.__cur = self.__node.val
                self.__node = self.__node.right if self.__forward else self.__node.left
                break
        return self.__cur


if __name__ == "__main__":

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

    itr = BSTIterator2(n1, True)
    while itr.hasNext():
        print(itr.next())

    itr = BSTIterator2(n1, False)
    while itr.hasNext():
        print(itr.next())