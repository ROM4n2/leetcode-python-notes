class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        maxLen = 0

        for right in range(len(s)):
            # s[right] 要加入窗口
            # 但如果 s[right] 已经在 window 里，收缩 left
            while s[right] in window:
                window.remove(s[left])
                left += 1
            # 现在 s[right] 不在 window 里了，加入
            window.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen
