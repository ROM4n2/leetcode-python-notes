class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        i, j = 0, len(height) - 1
        maxS = 0
        while i != j:
            maxS = max(maxS, (j - i) * min(height[i], height[j]))

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return maxS