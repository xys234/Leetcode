"""

21. Merge Two Sorted Lists (Easy)

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)  # self.next is converted and it triggers recursive calls


class Solution:
    def traverse(self, l):
        res = []
        while l:
            res.append(l.val)
            l = l.next
        return res

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None

        res = ListNode(0)
        it1 = l1
        it2 = l2
        it3 = res

        while it1 and it2:
            if it1.val < it2.val:
                it3.val = it1.val
                it1 = it1.next
            else:
                it3.val = it2.val
                it2 = it2.next
            it3.next = ListNode(0)
            it3 = it3.next
        while it1 and it2 is None:
            it3.val = it1.val
            it1 = it1.next
            if it1:
                it3.next = ListNode(0)
                it3 = it3.next
        while it2 and it1 is None:
            it3.val = it2.val
            it2 = it2.next
            if it2:
                it3.next = ListNode(0)
                it3 = it3.next
        return res

    def mergeTwoLists2(self, l1, l2):
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

if __name__ == "__main__":
    sol = Solution()

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(4)
    n1.next = n2
    n2.next = n3

    n4 = ListNode(1)
    n5 = ListNode(3)
    n6 = ListNode(5)
    n4.next = n5
    n5.next = n6

    print(n1)
    print(n4)
    print(sol.mergeTwoLists(n1, n4))
    print(sol.mergeTwoLists2(n1, n4))

        