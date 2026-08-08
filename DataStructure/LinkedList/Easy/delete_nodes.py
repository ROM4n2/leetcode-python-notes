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
    @param head: Head of a linked list.
    @param m: Nodes to be kept.
    @param n: Nodes to be deleted.
    @return: The head of the modified list after removing the mentioned nodes.
    """
    def delete_nodes(self, head: ListNode, m: int, n: int) -> ListNode:
        # --- write your code here ---
        if head: 
            curr = head
        else:
            return None
        while curr:
            for _ in range(m - 1):
                if not curr:
                    return head
                curr = curr.next
            if not curr:
                return head
            
            kept_tail = curr
            curr = curr.next

            for _ in range(n):
                if not curr:
                    break
                curr = curr.next

            kept_tail.next = curr         
        return head
        '''def remainNodes(head: ListNode, m: int) -> ListNode:
            curr = head
            for _ in range(m):
                if curr and curr.next:
                    curr = curr.next
                else:
                    return head
            return curr

        def deleteNodes(head: ListNode, n: int) -> ListNode|None:
            for _ in range(n):
                if head and head.next:
                    head = head.next
                else:
                    return None
            return head
        
        while curr is not None:
            tmp = curr
            curr = remainNodes(curr, m)
            if curr == tmp :
                return head
            curr = deleteNodes(curr, n)
            if curr == None:
                return head
        return head'''