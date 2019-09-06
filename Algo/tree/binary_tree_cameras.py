"""

968. Binary Tree Cameras

Given a binary tree, we install cameras on the nodes of the tree.

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "TreeNode({:d})".format(self.val)

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        """

        :param root:
        :return:

        Greedy algorithm

        """

        if not root.left and not root.right:
            return 1

        # level-order traversal to store all the nodes
        nums = []
        parents = {root: None}
        q = deque([root])

        while q:
            node = q.popleft()
            if node.left:
                parents[node.left] = node
                q.append(node.left)
            if node.right:
                parents[node.right] = node
                q.append(node.right)
            nums.append(node)

        cameras = {}
        for i in range(len(nums)-1, -1, -1):
            parent = parents[nums[i]]
            if nums[i] not in cameras and nums[i].left not in cameras and nums[i].right not in cameras:
                cameras[parent] = 1

        return sum(cameras.values())


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    n1.right = n2
    n2.right = n3
    n3.right = n4

    sol = Solution()
    print(sol.minCameraCover(n1))

