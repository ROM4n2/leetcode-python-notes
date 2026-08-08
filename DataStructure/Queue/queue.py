class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """
    def enqueue(self, item):
        # write your code here
        # ===== 链表实现 =====
        # node = [value, next]，用 list 模拟链表节点（可修改，tuple 不可改）
        node = [item, None]
        tail = getattr(self, 'tail', None)
        if tail is None:
            self.head = node
            self.tail = node
        else:
            tail[1] = node   # 当前 tail 的 next 指向新节点
            self.tail = node # tail 后移

        # ===== 原列表实现 =====
        # self.queue.append(item)

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        # ===== 链表实现 =====
        head = getattr(self, 'head', None)
        if head is None:
            return -1
        val = head[0]           # 取头节点值
        self.head = head[1]     # head 后移
        if self.head is None:
            self.tail = None    # 队列已空，tail 置空
        return val

        # ===== 原列表实现 =====
        # if len(self.queue) == 0:
        #     return -1
        # else:
        #     return self.queue.pop(0)
