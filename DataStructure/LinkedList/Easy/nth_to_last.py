'''from lintcode import (
    ListNode,
)'''

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
    @param head: The first node of linked list.
    @param n: An integer
    @return: Nth to last node of a singly linked list. 
    """
    def nth_to_last(self, head: ListNode, n: int) -> ListNode:
        # write your code here
        curr = head
        for _ in range(n):
            curr = curr.next
        prev = head
        while curr:
            curr = curr.next
            prev = prev.next
        return prev
    # 双指针 （ 快慢指针 ）