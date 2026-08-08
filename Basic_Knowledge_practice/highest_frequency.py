from typing import (
    List,
)

class Solution:
    """
    @param ip_lines: ip  address
    @return: return highestFrequency ip address
    """
    def highest_frequency(self, ip_lines: List[str]) -> str:
        # Write your code here
        di = {}
        for ip in ip_lines:
            di[ip] = di.get(ip, 0) + 1
        max_ip = None
        max_cnt = 0
        for ip, cnt in di.items():
            if cnt > max_cnt:
                max_cnt = cnt
                max_ip = ip
        return str(max_ip)
