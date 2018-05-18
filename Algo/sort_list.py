"""
148. Sort List (Medium)

Sort a linked list in O(n log n) time using constant space complexity.

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
    def createList(self, data):
        """

        :param data: a list
        :return: a head node to a linked list
        """
        nodes = [ListNode(i) for i in data]
        i = 0
        while i < len(nodes) - 1:
            nodes[i].next = nodes[i+1]
            i += 1
        return nodes[0]

    def splitList(self, head):
        front = fast = slow = head
        while fast.next:
            fast = fast.next
            if fast.next:
                slow = slow.next
                fast = fast.next
        back = slow.next        # Store the second list
        slow.next = None        # Terminate the first list
        return front, back

    def mergeLists(self, l1, l2):
        head = dummy = ListNode(0)      # one pointer and one iterator
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 or l2
        return dummy.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        elif head.next is None:
            return head
        front, back = self.splitList(head)
        front = self.sortList(front)
        back = self.sortList(back)
        return self.mergeLists(front, back)


if __name__=="__main__":
    sol = Solution()
    l = sol.createList([4,2,7,3,1,6])
    print("Initial List: " + repr(l))
    print("Sorted List:  " + repr(sol.sortList(l)))


