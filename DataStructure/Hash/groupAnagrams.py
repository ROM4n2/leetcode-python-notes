class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            key = ''.join(sorted(s))
            seen.setdefault(key, []).append(s)
        return list(seen.values())

    # 面试官最优解：字符计数法，时间 O(n·k)，避免排序
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     seen = {}
    #     for s in strs:
    #         count = [0] * 26
    #         for c in s:
    #             count[ord(c) - ord('a')] += 1 # 映射成 0~25
    #         key = tuple(count) # tuple 是不可变的列表 key 必须不可变
    #         seen.setdefault(key, []).append(s)
    # # 如果 key 存在，返回它的值；如果不存在，插入 key: default 并返回 default。
    #     return list(seen.values())