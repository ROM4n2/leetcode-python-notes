'''from lintcode import (
    ListNode,
)
'''
"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param node1: The first ListNode
    @param node2: The second ListNode
    @return: A new linked list representing the sum of corresponding numbers in the two given linked lists.
    """
    def sum_of_numbers(self, node1: ListNode, node2: ListNode) -> ListNode:
        # --- write your code here ---
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while node1 or node2 or carry:
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            total = val1 + val2 + carry
            curr.next = ListNode(total % 10)
            carry = total // 10
            curr = curr.next
            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next
        return dummy.next