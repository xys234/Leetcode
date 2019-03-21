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

        if not root:
            return ''

        s = []
        self.serialize_helper(root, s)
        return ','.join(s)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if len(data) == 0:
            return None

        pos = 0
        return self.deserialize_helper(list(data.split(',')), -float('inf'), float('inf'))

    def serialize_helper(self, root, s):
        if root is None:
            return
        s.append(str(root.val))
        self.serialize_helper(root.left, s)
        self.serialize_helper(root.right, s)
        return s

    def deserialize_helper(self, data, cur_min, cur_max):
        if not data:
            return None
        val = int(data[0])
        if val < cur_min or val > cur_max:
            return None
        data.pop(0)
        root = TreeNode(val)
        root.left = self.deserialize_helper(data, cur_min, val)
        root.right = self.deserialize_helper(data, val, cur_max)
        return root


def preorder(root, seq):

    if root is None:
        return

    seq.append(str(root.val))
    preorder(root.left, seq)
    preorder(root.right, seq)


if __name__ == '__main__':

    n1 = TreeNode(41)
    n2 = TreeNode(42)
    n3 = TreeNode(43)
    n4 = TreeNode(44)
    n5 = TreeNode(5)

    n3.left, n3.right = n1, n4
    n1.right = n2

    # n2.left, n2.right = n1, n3

    seq = []
    preorder(n3, seq)
    print(','.join(seq))

    codec = Codec()
    tree_serialized = codec.serialize(n3)
    print(tree_serialized)
    root = codec.deserialize(tree_serialized)

    seq = []
    preorder(root, seq)
    print(','.join(seq))