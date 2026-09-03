# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Reverse the second half
        prev = self.reverse(slow)
        # Compare the first and second halves
        left = head
        right = prev
        res = True
        while right:
            if left.val != right.val:
                res = False
                break
            left= left.next
            right = right.next
        # Restore
        self.reverse(prev)
        return res

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next_tmp = head.next
            head.next = prev
            prev = head
            head = next_tmp
        return prev
