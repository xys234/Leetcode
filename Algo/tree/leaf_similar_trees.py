"""

872

Consider all the leaves of a binary tree.
From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

"""


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        # find all the leaves for each tree and then compare
        def get_leaf_nodes(root, leaves):
            if not root:
                return
            if root.left is None and root.right is None:
                leaves.append(root.val)
            get_leaf_nodes(root.left, leaves)
            get_leaf_nodes(root.right, leaves)

        leaves1, leaves2 = [], []
        get_leaf_nodes(root1, leaves1)
        get_leaf_nodes(root2, leaves2)
        return leaves1 == leaves2

    def leafSimilar2(self, root1, root2):
        seq1, seq2 = [], []

        def inorder_traversal(root, leaves):
            if not root:
                return

            inorder_traversal(root.left, leaves)
            if not root.left and not root.right:
                leaves.append(root.val)
            inorder_traversal(root.right, leaves)

        inorder_traversal(root1, seq1)
        inorder_traversal(root2, seq2)

        return seq1 == seq2


