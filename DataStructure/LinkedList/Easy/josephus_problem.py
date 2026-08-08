"""
约瑟夫环问题 — 循环链表模拟

问题描述：
  n 个人围成一圈，从第一个人开始报数，数到 k 的人出列，
  然后下一个人重新从 1 开始报数，直到只剩一个人。

思路（循环链表模拟）：
  1. 构建一个单向循环链表，节点编号为 1 ~ n
  2. 从 head 开始遍历，每走 k-1 步到达要删除的节点
  3. 删除该节点（将前一个节点的 next 跳过它）
  4. 从下一个节点继续，重复直到只剩一个节点
"""
"""
用循环链表模拟约瑟夫环，返回最后幸存者的编号。
"""
    # ------------------------------------------------------------
    # 第 1 步：构建循环链表 1 -> 2 -> ... -> n -> head
    # ------------------------------------------------------------

    # ------------------------------------------------------------
    # 第 2 步：开始模拟淘汰过程
    #   用 cur 指向当前报数的人
    #   用 prev 指向 cur 的前一个节点（方便删除）
    #   每走 k-1 步，删除 cur 指向的节点，继续下一轮
    # ------------------------------------------------------------

    # ------------------------------------------------------------
    # 第 3 步：环中只剩一个人，返回其编号
    # ------------------------------------------------------------

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @return: Number of the last person left behind
    """
    def josephus_problem(self, n: int, m: int) -> int:
        # write your code here
        class ListNode:
            def __init__(self, val, next = None) -> None:
                self.val = val
                self.next = next
        head = ListNode(1)
        prev = head
        for i in range(2,n+1):
            prev.next = ListNode(i)
            prev = prev.next
        prev.next = head

        cur = head
        # prev =prev

        assert prev is not None
        while prev.next != prev:
            for _ in range(m-1):
                prev = cur
                cur = cur.next
            
            prev.next = cur.next
            cur = prev.next
        return cur.val
