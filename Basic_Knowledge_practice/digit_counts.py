class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digit_counts(self, k: int, n: int) -> int:
        # write your code here
        cnt = 0
        for i in range(n + 1):
            cnt += str(i).count(str(k)) # 总出现次数用count最为合适
            # find适合判断有没有出现
        return cnt