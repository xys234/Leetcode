"""

109.

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5


"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: 'ListNode') -> 'TreeNode':
        if not head:
            return None

        def helper(node):
            if not node:
                return None
            prev, mid_node = self.mid(node)
            root = TreeNode(mid_node.val)
            if prev:
                prev.next = None
                root.left = helper(node)
            root.right = helper(mid_node.next)
            return root

        return helper(head)

    @staticmethod
    def mid(head: 'ListNode') -> ('ListNode',):
        prev = None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next

            if not fast:
                break
            prev = slow
            slow = slow.next
        return prev, slow


def inorder(root: 'TreeNode', seq: 'list'):
    if not root:
        return
    inorder(root.left, seq)
    seq.append(root.val)
    inorder(root.right, seq)


def to_linked_list(nums: 'list') -> 'ListNode':
    nodes = list(map(ListNode, nums))
    for i, node in enumerate(nodes):
        if i == len(nodes) - 1:
            break
        node.next = nodes[i+1]
    return nodes[0]


if __name__ == '__main__':

    sol = Solution()

    cases = [


        (sol.sortedListToBST, (to_linked_list([-10, -3, 0, 5, 9]), ), [-10, -3, 0, 5, 9]),
        (sol.sortedListToBST, (to_linked_list([-12, -10, -3, 0, 5, 9]), ), [-12, -10, -3, 0, 5, 9]),

    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        inorder_seq = []
        inorder(ans, inorder_seq)
        if inorder_seq == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(inorder_seq)))