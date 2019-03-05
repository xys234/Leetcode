"""

449.

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed
later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be
serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.


"""

import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        pre-order traversal

        :type root: TreeNode
        :rtype: str
        """

        s = []
        self.serialize_helper(root, s)
        return ''.join(s)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        pos = 0
        return self.deserialize_helper(data, pos, -float('inf'), float('inf'))

    def serialize_helper(self, root, s):
        if root is None:
            return
        s.append(str(root.val))
        self.serialize_helper(root.left, s)
        self.serialize_helper(root.right, s)
        return s

    def deserialize_helper(self, data, pos, cur_min, cur_max):
        if pos >= len(data):
            return None
        val = int(data[pos])
        if val < cur_min or val > cur_max:
            return None
        pos += 1
        root = TreeNode(val)
        root.left = self.deserialize_helper(data, pos, cur_min, val)
        cur_max = float('inf')
        root.right = self.deserialize_helper(data, pos, val, cur_max)
        cur_min = -float('inf')
        return root

    def serialize(self, root):
        if not root:
            return ''

        toRet = str(root.val)
        if root.left:
            toRet += ',' + self.serialize(root.left)
        if root.right:
            toRet += ',' + self.serialize(root.right)
        return toRet

    def deserialize(self, data):

        def dfs(node, data, inf, sup):
            if data and inf < data[0].val < node.val:
                node.left = data.popleft()
                dfs(node.left, data, inf, node.val)

            if data and node.val < data[0].val < sup:
                node.right = data.popleft()
                dfs(node.right, data, node.val, sup)

        if data == '':
            return []

        data = collections.deque(map(TreeNode, map(int, data.split(','))))
        root = data.popleft()
        dfs(root, data, float('-inf'), float('inf'))

        return root

def preorder(root, seq):

    if root is None:
        return

    seq.append(str(root.val))
    preorder(root.left, seq)
    preorder(root.right, seq)

if __name__ == '__main__':

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    # n3.left, n3.right = n1, n4
    # n1.right = n2
    # n3.left = n5

    n2.left, n2.right = n1, n3

    seq = []
    preorder(n2, seq)
    print(''.join(seq))

    codec = Codec()
    tree_serialized = codec.serialize(n2)
    print(tree_serialized)
    root = codec.deserialize(tree_serialized)

    seq = []
    preorder(root, seq)
    print(''.join(seq))