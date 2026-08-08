from typing import (
    List,
)

class Solution:
    """
    @param s: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotate_string(self, s: List[str], offset: int):
        if not s:
            return
        n = len(s)
        offset %= n
        if offset == 0:
            return

        def reverse(l: int, r: int) -> None:
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, offset - 1)
        reverse(offset, n - 1)
       # 两次反转恢复原序 