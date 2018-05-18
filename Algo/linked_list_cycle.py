"""

141. Linked List Cycle (Easy)

Given a linked list, determine if it has a cycle in it.

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
    def hasCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return True
        return False