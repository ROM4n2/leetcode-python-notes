class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []
        nums.sort()

        result = []

        for i in range(len(nums) - 1):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

# 题解：三数之和 (LeetCode 15)
#
# 核心思想：排序 + 双指针，将三数问题降为两数问题
#
# 算法步骤：
#   1. 排序数组，使双指针和去重成为可能
#   2. 遍历每个数 nums[i] 作为第一个固定数
#   3. 在 nums[i] 右侧用双指针 (left, right) 寻找两数之和为 -nums[i]
#      - total < 0：和太小，left 右移找更大的数
#      - total > 0：和太大，right 左移找更小的数
#      - total == 0：找到一组解，left 和 right 同时向中间移动
#   4. 去重：排序后相同值相邻，跳过即可
#      - 外层：nums[i] == nums[i-1] 时跳过
#      - 内层：找到解后，跳过与当前 left/right 相同的值
#
# 复杂度：
#   时间 O(n²)：外层遍历 O(n)，内层双指针 O(n)
#   空间 O(1)：不算输出数组，排序为原地
#
# 关键点：
#   - 先 append 再移动指针，否则记录的是错误的值
#   - 找到解后 left 和 right 必须同时移动，否则死循环
#   - 去重在移动之后进行，比较 nums[left] 和 nums[left-1]
    