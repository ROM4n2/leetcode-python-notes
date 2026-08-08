from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @param index1: the first index
    @param index2: the second index
    @return: nothing
    """
    def swap_integers(self, a: List[int], index1: int, index2: int):
        # write your code here
        a[index1], a[index2] = a[index2], a[index1]