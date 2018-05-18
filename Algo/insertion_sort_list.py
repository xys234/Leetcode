"""

147. Insertion Sort List (Medium)

Sort a linked list using insertion sort.

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
        if len(data) == 0 or data is None:
            return None
        nodes = [ListNode(i) for i in data]
        i = 0
        while i < len(nodes) - 1:
            nodes[i].next = nodes[i+1]
            i += 1
        return nodes[0]

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        if head.next is None:
            return dummy.next
        max_itr = head.next
        itr = max_itr.next
        if itr is None:
            return dummy.next

        while itr:
            while itr.val > max_itr.val:
                max_itr = itr
                itr = itr.next
                if itr is None:
                    break
            if itr is None:
                break
            while head.next.val < itr.val:
                head = head.next

            # Insertion: imagine the sequence after the sort, construct the sequence from rightmost to left
            max_itr.next = itr.next
            itr.next = head.next
            head.next = itr

            # Update minimum and maximum pointers
            head = dummy
            itr = max_itr.next
        return dummy.next

    def insertionSortList2(self, head):
        if head is None or self.isSorted(head):
            return head

        dummy = ListNode(-2147483648)
        dummy.next = head
        cur, sorted_tail = head.next, head
        while cur:
            prev = dummy
            while prev.next.val < cur.val:
                prev = prev.next
            if prev == sorted_tail:
                cur, sorted_tail = cur.next, cur
            else:
                cur.next, prev.next, sorted_tail.next = prev.next, cur, cur.next
                cur = sorted_tail.next

        return dummy.next

    def isSorted(self, head):
        while head and head.next:
            if head.val > head.next.val:
                return False
            head = head.next
        return True



if __name__ == "__main__":

    sol = Solution()
    l = sol.createList([4, 2, 7, 3, 1, 6])
    print("Initial List: " + repr(l))
    print("Sorted List:  " + repr(sol.insertionSortList2(l)))
    #
    # l = sol.createList([3,4,1])
    # print("Initial List: " + repr(l))
    # print("Sorted List:  " + repr(sol.insertionSortList(l)))

    # l = sol.createList([3,2, 4])
    # print("Initial List: " + repr(l))
    # print("Sorted List:  " + repr(sol.insertionSortList(l)))

    # l = sol.createList([6,5,4,3,2,1])
    # print("Initial List: " + repr(l))
    # print("Sorted List:  " + repr(sol.insertionSortList(l)))

    l = sol.createList([])
    print("Initial List: " + repr(l))
    print("Sorted List:  " + repr(sol.insertionSortList(l)))