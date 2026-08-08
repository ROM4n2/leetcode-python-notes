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
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head: ListNode, x: int) -> ListNode:
        # write your code here
        before_dummy = ListNode(0)
        after_dummy = ListNode(0)
        before = before_dummy
        after = after_dummy

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        # 切断大于等于链表的尾部，避免形成环
        after.next = None
        # 连接小于链表和大于等于链表
        before.next = after_dummy.next

        return before_dummy.next