class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        ans = 0
        d = {0: 1}
        prefix_sum = 0 #前缀和
        for num in nums:
            prefix_sum += num
            print("prefix_sum:", prefix_sum)

            if prefix_sum - k in d:
                ans += d[prefix_sum - k]
                print("ans:", ans)
            d[prefix_sum] = d.get(prefix_sum, 0) + 1
        return ans

if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 3
    solution = Solution()
    result = solution.subarraySum(nums, k)
    print(result)  # Output: 2
