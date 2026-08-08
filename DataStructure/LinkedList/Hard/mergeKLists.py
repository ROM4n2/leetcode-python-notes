# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if list1 is None:
                return list2
            if list2 is None:
                return list1
            if list1.val < list2.val:
                list1.next = mergeTwoLists(list1.next, list2)
                return list1
            list2.next = mergeTwoLists(list1, list2.next)
            return list2
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    merged.append(mergeTwoLists(lists[i], lists[i + 1]))
                else:
                    merged.append(lists[i])
            lists = merged
        return lists[0]