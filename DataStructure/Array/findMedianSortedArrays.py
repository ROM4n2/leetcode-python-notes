class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保证 nums1 是较短的数组，降低二分复杂度
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2  # 左半部分需要的元素个数

        lo, hi = 0, m
        while lo <= hi:
            # i 是 nums1 的分割点，j 是 nums2 的分割点
            i = (lo + hi) // 2
            j = total_left - i

            # 处理边界：当分割点在边界时，用无穷大/无穷小代替
            nums1_left_max  = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right_min = nums1[i]     if i < m else float('inf')
            nums2_left_max  = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right_min = nums2[j]     if j < n else float('inf')

            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # 找到了正确的分割
                if (m + n) % 2 == 0:
                    # 偶数长度：中位数 = 左最大与右最小的平均值
                    return (max(nums1_left_max, nums2_left_max) +
                            min(nums1_right_min, nums2_right_min)) / 2.0
                else:
                    # 奇数长度：中位数 = 左半部分的最大值
                    return max(nums1_left_max, nums2_left_max)
            elif nums1_left_max > nums2_right_min:
                # nums1 左边太大，分割点左移
                hi = i - 1
            else:
                # nums2 左边太大，分割点右移
                lo = i + 1
