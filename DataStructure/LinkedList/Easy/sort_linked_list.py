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
    @param head: A linked list sorted by the absolute value of the node values
    @return: Returns a linked list sorted by node value
    """
    def sort_linked_list(self, head: ListNode) -> ListNode:
        if not head:
            return head
        # 如果头节点为空，直接返回

        neg_dummy = ListNode(0)
        pos_dummy = ListNode(0)
        pos_tail = pos_dummy

        curr = head
        while curr:
            nxt = curr.next
            if curr.val < 0:
                # 头插法插入 neg 链表（自动逆序）
                curr.next = neg_dummy.next
                neg_dummy.next = curr
            else:
                # 尾插法插入 pos 链表（保持原序）
                pos_tail.next = curr
                pos_tail = curr
                pos_tail.next = None
            curr = nxt

        neg_head = neg_dummy.next
        pos_head = pos_dummy.next

        if not neg_head:
            return pos_head
        if not pos_head:
            return neg_head

        # 找到 neg 链表尾部，接上 pos 链表
        tail = neg_head
        while tail.next:
            tail = tail.next
        tail.next = pos_head

        return neg_head