# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr1 = dummy.next# if curr1.next else None
        curr2 = curr1.next if curr1 and curr1.next else None
        while curr1 and curr2:
            # swap
            temp = curr2.next# if curr2.next else None
            prev.next = curr2
            curr2.next = curr1
            curr1.next = temp
            # next
            prev = curr1
            curr1 = temp
            curr2 = temp.next if temp else None
        return dummy.next