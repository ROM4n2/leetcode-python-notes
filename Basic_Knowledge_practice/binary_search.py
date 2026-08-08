from typing import (
    List,
)

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binary_search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1
    
    '''
    # write your code here
        left = 0
        right = len(nums) - 1
        while left != right:
            mid = int(left + right) # mid 没除以2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # 往右边找
                right = mid # 改为left = mid + 1
            else:
                left = mid # 改为right = mid
        mid = int(left + right) # mid 没除以2
        if nums[mid] == target:
            return mid
        return -1
        '''