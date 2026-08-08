from typing import (
    List,
)

class Solution:
    """
    @param n: an integer
    @return: return all prime numbers within n.
    """
    def prime(self, n: int) -> List[int]:
        # write your code here
        ls = []
        if n <= 1:
            return ls
        flag = 0
        for i in range(2,n+1): # python 左闭右开
            flag = 0
            for j in range(2,int(i**0.5)+1):
                if i%j == 0:
                    flag = 1
                    break
            if flag == 1:
                continue
            else:
                ls.append(i)
        return ls