class Solution:
    """
    @param n: an integer
    @return: an integer f(n)
    """
    def fibonacci(self, n: int) -> int:
        # write your code here
        if n == 1:
            return 0
        if n == 2:
            return 1
        a, b = 0, 1
        for _ in range(3, n + 1): # _ 下划线表示用不到这个 i
            a, b = b, a + b # 并行赋值 同时做a = b, b = a+b
        return b
    #- 时间复杂度从 O(2^n) → O(n)
    #- 空间复杂度从 O(n)（递归栈）→ O(1)
'''    
    def fibonacci(self, n: int) -> int:
        # write your code here
        if n == 1:
            return 0
        if n == 2:
            return 1
        return self.fibonacci(n-1) + self.fibonacci(n-2)
        # 时间复杂度 O(2^n)
        # fib(n-1) + fib(n-2) 有大量重复计算（fib(3) 被算了 N 次）
'''