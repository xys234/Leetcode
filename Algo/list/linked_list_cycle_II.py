"""

142. Linked List Cycle II (Medium)

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # def __repr__(self):
    #     if self:
    #         return "{} -> {}".format(self.val, self.next)

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:            # this iteration scheme guarantees the meet if there is a cycle
                fast = head
                while fast is not slow: # This guarantees to reach the starting node of the cycle
                    fast, slow = fast.next, slow.next
                return fast
        return None

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
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n2
    # n6.next = n2

    print(sol.detectCycle(n1))
