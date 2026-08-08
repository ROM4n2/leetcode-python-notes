from lintcode import (
    ListNode,
)

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
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def remove_elements(self, head: ListNode, val: int) -> ListNode:
        # write your code here
        curr = head
        dummy = ListNode(0)
        tail = dummy
        while curr:
            next_node = curr.next
            if curr.val != val:
                tail.next = curr
                curr.next = None
                tail = tail.next
            curr = next_node
        tail.next = None
        return dummy.next