import pytest

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ll1 = []
        while l1 != None:
            ll1.append(l1.val)
            l1 = l1.next

        ll2 = []
        while l2 != None:
            ll2.append(l2.val)
            l2 = l2.next

        n1 = int(''.join(str(l) for l in ll1[::-1]))
        n2 = int(''.join(str(l) for l in ll2[::-1]))

        sum = n1+ n2

        l3 = None
        for s in str(sum):
            lnext = l3
            l3 = ListNode(int(s))
            l3.next = lnext

        return l3


def test_solution():
    
    a = Solution()

    l10 = ListNode(2)
    l11 = ListNode(4)
    l12 = ListNode(3)
    l10.next = l11
    l11.next = l12

    l20 = ListNode(5)
    l21 = ListNode(6)
    l22 = ListNode(4)
    l20.next = l21    
    l21.next = l22

    l30 = ListNode(7)
    l31 = ListNode(0)
    l32 = ListNode(8)
    l30.next = l31    
    l31.next = l32

    assert(a.addTwoNumbers(l10, l20).val == l30.val)
    assert(a.addTwoNumbers(l10, l20).next.val == l30.next.val)
    assert(a.addTwoNumbers(l10, l20).next.next.val == l30.next.next.val)

    l30 = ListNode(2)
    l31 = ListNode(7)
    l32 = ListNode(3)
    l30.next = l31
    l31.next = l32

    l40 = ListNode(5)
    l41 = ListNode(6)
    l40.next = l41

    l50 = ListNode(7)
    l51 = ListNode(3)
    l52 = ListNode(4)
    l50.next = l51
    l51.next = l52

    assert(a.addTwoNumbers(l30, l40).val == l50.val)
    assert(a.addTwoNumbers(l30, l40).next.val == l50.next.val)
    assert(a.addTwoNumbers(l30, l40).next.next.val == l50.next.next.val)
        