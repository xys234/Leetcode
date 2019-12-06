"""

A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.


"""

class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        def make_copy(current_node):
            """
            Make copies of each node using DFS
            :param current_node:
            :return:
            """

            ptr = Node(None, current_node, None)
            while ptr.next:
                ptr = ptr.next
                if not hasattr(ptr, 'copy'):
                    ptr.copy = Node(ptr.val, None, None)

        def connect(current_node):
            ptr = Node(None, current_node, None)
            while ptr.next:
                ptr = ptr.next
                if ptr.next:
                    ptr.copy.next = ptr.next.copy
                if ptr.random:
                    ptr.copy.random = ptr.random.copy

        if not head:
            return head
        else:
            make_copy(head)
            connect(head)

