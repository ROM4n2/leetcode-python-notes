from typing import (
    List,
)
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
    @param head: the given linked list
    @return: the array that store the values in reverse order 
    """
    def reverse_store(self, head: ListNode) -> List[int]:
        # write your code here
        ls = []
        def dfs(node, result):
            if node is None:
                return
            else:
                dfs(node.next, result)
            result.append(node.val)
            return
        dfs(head, ls)
        return ls
    
    """
    stack = []
    ls = []
    curr = head
    while curr:
        stack.append(curr.val)
        curr = curr.next
    while stack:
        val = stack.pop()
        ls.append(val)
    return ls
    """