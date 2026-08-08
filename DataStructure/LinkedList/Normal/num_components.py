class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: the head
    @param g: an array
    @return: the number of connected components in G
    """
    def num_components(self, head: ListNode, g: List[int]) -> int:
        if not head:
            return 0

        g_set = set(g)
        count = 0
        prev_in_g = False  # 前一个节点是否在 G 中

        curr = head
        while curr:
            if curr.val in g_set:
                if not prev_in_g:
                    count += 1  # 新组件开始
                prev_in_g = True
            else:
                prev_in_g = False
            curr = curr.next

        return count
        