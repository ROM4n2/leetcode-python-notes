'''from lintcode import (
    ListNode,
)'''


'''
    dummy = ListNode(0)           # 哨兵
    curr = head                   # 遍历原链表
    while curr:
        next_node = curr.next     # 先保存原链表的下一个
        prev = dummy              # 从哨兵开始找插入位置
        while prev.next and prev.next.val < curr.val:
            prev = prev.next      # 找到第一个 >= curr.val 的节点的前驱
        curr.next = prev.next     # ① 新节点指向后继
        prev.next = curr          # ② 前驱指向新节点
        curr = next_node          # 处理原链表的下一个
    return dummy.next
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
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertion_sort_list(self, head: ListNode) -> ListNode:
        # write your code here
        dummy = ListNode(0)
        curr = head
        while curr:
            next_node = curr.next
            prev = dummy
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next
            
            curr.next = prev.next
            prev.next = curr
            
            curr = next_node
        return dummy.next