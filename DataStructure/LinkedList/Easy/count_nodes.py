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
    @param head: the first node of linked list.
    @return: An integer
    """
    def count_nodes(self, head: ListNode) -> int:
        # write your code here
        cnt = 0
        curr = head
        while curr is not None:
            cnt +=1
            curr = curr.next
        return cnt
    
'''
class Solution:
      def count_nodes(self, head: ListNode | None) -> int:
          cnt = 0
          while head is not None:
              cnt += 1
              head = head.next
          return cnt
'''