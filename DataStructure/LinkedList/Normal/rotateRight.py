# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        fast = slow = head
        if head is None or k == 0 or head.next is None:
            return head
        len = 0
        curr = head
        while curr:
            curr = curr.next
            len+=1

        if k % len == 0:
            return head
        
        for _ in range(k%len):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next

        dummy.next = slow.next
        slow.next = None
        fast.next = head
        return dummy.next