# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode(0, head)
            prev = dummy
            curr = head

            while curr:
                if curr.next and curr.val == curr.next.val:
                    # 有重复，跳过所有相同值的节点
                    while curr.next and curr.val == curr.next.val:
                        curr = curr.next
                    # curr 指向最后一个重复节点，跳过它
                    prev.next = curr.next
                else:
                    # 无重复，prev 安全前进
                    prev = curr
                curr = curr.next

            return dummy.next