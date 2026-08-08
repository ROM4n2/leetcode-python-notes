from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizz_buzz(self, n: int) -> List[str]:
        # write your code here
        ls = []
        for i in range(1, n+1):
            s = "fizz" * (i % 3 == 0) + " " * (i % 3 == 0 and i % 5 == 0) + "buzz" * (i % 5 == 0)
            ls.append(s or str(i))
        return ls
        
        """ls = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                ls.append("fizz buzz")
            elif i % 3 == 0:
                ls.append("fizz")
            elif i % 5 == 0:
                ls.append("buzz")
            else:
                ls.append(str(i))
        return ls"""