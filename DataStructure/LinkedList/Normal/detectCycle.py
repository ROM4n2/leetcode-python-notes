# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

        '''
        seen = set()
        while head:
            if head in seen:    # ← 这个节点对象已经见过了
                return head     # ← 这就是入环点
            seen.add(head)
            head = head.next
        return None
        '''