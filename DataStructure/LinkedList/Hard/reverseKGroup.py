# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0, head)
        fast = slow = head
        before = dummy
        while True:
            for _ in range(k):
                if not fast:
                    return dummy.next
                fast = fast.next
            prev = None
            curr = slow
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            before.next = prev      # 把前半段接到翻转后的新头
            slow.next = curr        # 翻转后的尾巴接到下一组
            before = slow           # 更新 before 为当前组的尾巴，供下一组使用
            slow = fast = curr