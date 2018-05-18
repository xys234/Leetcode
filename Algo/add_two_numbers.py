# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Example
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# ----------------- INPUTS ----------------------
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self, **kwargs):
        res = str(self.val)
        p = self
        while p.next:
            res += str(p.next.val)
            p = p.next
        return res

    def num(self):
        res = str(self.val)
        p = self
        while p.next:
            res += str(p.next.val)
            p = p.next
        return int(res[::-1])



# ------------------ ATTEMPT ---------------------
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)		
        r1 = result 

        carry = ListNode(0)
        c1 = carry

        p1 = l1
        p2 = l2

        while p1 or p2:

            c2 = ListNode(0)
            c1.next = c2

            if p1 is None:
                sum = p2.val + c1.val 
            elif p2 is None:
                sum = p1.val + c1.val
            else:
                sum = p1.val + p2.val + c1.val


            if sum >= 10:
                r1.val = sum - 10
                c2.val = 1
            else:
                r1.val = sum
                c2.val = 0

            c1 = c2

            if p1:
                p1 = p1.next
            if p2:        
                p2 = p2.next

            if p1 or p2:
                r2 = ListNode(0)
                r1.next = r2
                r1 = r2
            elif c2.val > 0:
                r2 = ListNode(c2.val)
                r1.next = r2
                r1 = r2
            
        return result



if __name__ == "__main__":
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)

    l1 = n1
    n1.next = n2
    n2.next = n3

    # print(l1)
    
    n4 = ListNode(5)
    n5 = ListNode(6)
    n6 = ListNode(4)

    l2 = n4
    n4.next = n5
    n5.next = n6

    # print(l2)

    s = Solution()
    #res = s.addTwoNumbers(l1, l2)
    #assert res.num() == l1.num()+l2.num()


    # Test case 2  243 + 56
    #n5.next = None
    #res = s.addTwoNumbers(l1, l2)
    #print(str(l1.num())+"+"+str(l2.num())+"="+str(res.num()))
    #print("\n")


    # Test case 3: 5+5
    n1 = ListNode(5)
    n1.next = None
    l1 = n1
    l2 = n1

    res = s.addTwoNumbers(l1, l2)
    print(str(l1.num())+"+"+str(l2.num())+"="+str(res.num()))




