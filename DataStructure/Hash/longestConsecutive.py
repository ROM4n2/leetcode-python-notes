class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        st = set(nums)
        if len(st) == 1:
            return 1
        maxLen = 1
        for num in st:
            if num - 1 not in st:
                i = 1
                while num + i in st:
                    maxLen = max(i + 1, maxLen)
                    i+=1
        return maxLen