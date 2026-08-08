# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

        # fast = head
        # slow = head
        # dummy = ListNode(0)
        # curr = dummy
        # for _ in range(n):
        #     fast = fast.next
        # while fast:
        #     next_node = slow.next
        #     curr.next = slow
        #     curr = curr.next
        #     curr.next = None
        #     fast = fast.next
        #     slow = next_node

        # slow = slow.next
        # while slow:
        #     next_node = slow.next
            
        #     curr.next = slow
        #     curr = curr.next
        #     curr.next = None
        #     slow = next_node
        # return dummy.next