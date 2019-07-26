"""

1110.

Medium

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

"""

from typing import List
from Algo.utilities.tree import *


class Solution:
    def delNodes_fail(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root is None:
            return []

        left, right = [], []
        if root.left:
            left = self.delNodes(root.left, to_delete)
            if root.left.val in to_delete:
                root.left = None

        if root.right:
            right = self.delNodes(root.right, to_delete)
            if root.right.val in to_delete:
                root.right = None

        if root.val in to_delete:
            return left + right
        elif len(left) <= 1 and len(right) > 1:
            return [root] + right
        elif len(left) > 1 and len(right) <= 1:
            return [root] + left
        elif len(left) <= 1 and len(right) <= 1:
            return [root]
        else:
            return [root] + left + right

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ## returns True if the node is deleted, vice versa
        def del_node(node, to_delete, res):
            if not node: return False

            ## If the left child reports that it IS supposed to be deleted,
            # disown/delete the child (by replacing it with None)
            if del_node(node.left, to_delete, res):
                node.left = None
            ## Do the same for the right node
            if del_node(node.right, to_delete, res):
                node.right = None

            ## if this node is in to_delete,
            # add it's children into our result
            if node.val in to_delete:
                if node.left: res.append(node.left)
                if node.right: res.append(node.right)
                return True  # report back to my parent that I am deleted
            else:
                return False  # report back to my parent that I am not deleted

        res = []
        # use set instead of list so lookups are O(1) instead of O(n)
        to_delete = set(to_delete)
        is_del = del_node(root, to_delete, res)
        if not is_del: res.append(root)

        return res


if __name__ == "__main__":
    sol = Solution()
    method = sol.delNodes

    tree1 = deserialize('[1,2,3,4,5,6,7]')
    print(method(tree1, [3, 5]))
