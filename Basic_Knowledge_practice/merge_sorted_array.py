from typing import (
    List,
)

class Solution:
    """
    @param a: sorted integer array A
    @param b: sorted integer array B
    @return: A new sorted integer array
    """
    def merge_sorted_array(self, a: List[int], b: List[int]) -> List[int]:
        # write your code here
        ls = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                ls.append(a[i])
                i += 1
            elif a[i] > b[j]:
                ls.append(b[j])
                j += 1
            else:
                ls.append(a[i])
                ls.append(b[j])
                i += 1
                j += 1
        while i < len(a):
            ls.append(a[i])
            i += 1
        while j < len(b):
            ls.append(b[j])
            j += 1
        return ls