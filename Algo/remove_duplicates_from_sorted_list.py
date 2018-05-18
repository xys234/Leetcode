"""
83. Remove Duplicates from Sorted List (Easy)

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        head = dummy        # reuse head the other iterator
        itr = head.next

        while itr.next:
            if head.next.val == itr.next.val:
                head.next, itr = itr.next, itr.next
            else:
                head, itr = head.next, itr.next
        return dummy.next

    def createList(self, data):
        """
        :param data: a list
        :return: a head node to a linked list
        """
        if len(data) == 0 or data is None:
            return None
        nodes = [ListNode(i) for i in data]
        i = 0
        while i < len(nodes) - 1:
            nodes[i].next = nodes[i+1]
            i += 1
        return nodes[0]

if __name__ == "__main__":

    sol = Solution()
    l = sol.createList([1, 2, 2, 2, 3, 3])
    print("Initial List  : " + repr(l))
    print("Processed List: " + repr(sol.deleteDuplicates(l)))

    # l = sol.createList([1, 1])
    # print("Initial List  : " + repr(l))
    # print("Processed List: " + repr(sol.deleteDuplicates(l)))