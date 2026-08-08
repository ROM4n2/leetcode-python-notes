'''
from lintcode import (
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
    @param head_a: Head of a linked list
    @param head_b: Head of a linked list
    @return: Nodes when two linked lists intersect
    """
    def get_intersect_node(self, head_a: ListNode, head_b: ListNode) -> ListNode:
        # write your code here
        # 双指针法：将两个链表拼接（A+B 和 B+A）消除长度差，相交时会在交点相遇
        #
        # 设 A 独有 m 步，B 独有 n 步，公共部分 k 步
        #   pa 路径: A (m+k) → B.head (n)    = m+k+n 步
        #   pb 路径: B (n+k) → A.head (m)    = n+k+m 步
        # 步数相等 → 若有交点，必同时到达；若无交点，同时走到 None
        if head_a is None or head_b is None:
            return None  # type: ignore

        pa, pb = head_a, head_b
        while pa is not pb:
            pa = pa.next if pa else head_b
            pb = pb.next if pb else head_a

        return pa  # type: ignore 