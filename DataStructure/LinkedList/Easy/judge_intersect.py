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
    @return: Whether two linked lists intersect
    """
    def judge_intersect(self, head_a: ListNode, head_b: ListNode) -> bool:
        # write your code here
        if head_a == None or head_b == None:
            return False
        else:
            while head_a is not None: # 等价于 while head_a or (head_b is not None):
                curr = head_b
                while curr is not None:
                    if curr == head_a:
                        return True
                    curr = curr.next
                head_a = head_a.next
            return False 