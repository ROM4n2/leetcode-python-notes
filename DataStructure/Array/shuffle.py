class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ls = []
        for i in range(n):
            ls.append(nums[i])
            ls.append(nums[i + n])
        return ls

'''
zipped = zip(nums[:n], nums[n:])
result = [x for pair in zipped for x in pair]
return result
'''