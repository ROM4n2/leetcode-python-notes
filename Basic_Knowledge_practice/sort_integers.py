from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers(self, a: List[int]):
        # write your code here
        for i in range(len(a)):
            for j in range(len(a) - 1 - i):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
