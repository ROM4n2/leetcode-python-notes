from typing import (
    List,
)

class Solution:
    """
    @param array: An array.
    @return: An interger.
    """
    def find_number(self, array: List[int]) -> int:
        # Write your code here.
        max_num = 0
        di = {}
        for num in array:
            di[num] = di.get(num, 0) + 1
        max_cnt = 0
        for num, cnt in di.items():
            if cnt>max_cnt:
                max_cnt = cnt
                max_num = num
            elif cnt == max_cnt:
                max_num = min(max_num, num)
        return max_num
