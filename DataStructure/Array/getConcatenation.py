class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ls = []
        for num in nums:
            ls.append(num)
        for num in nums:
            ls.append(num)
        return ls
'''
return nums * 2
'''