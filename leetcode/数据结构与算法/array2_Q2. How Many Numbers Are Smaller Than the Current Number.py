# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        lis = nums.copy()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    ans[i] += 1
                elif nums[i] < nums[j]:
                    ans[j] += 1

        return ans

# 暴力解法
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         ans = []
#         for i in range(len(nums)):
#             count = 0
#             for j in range(len(nums)):
#                 if nums[j] < nums[i]:
#                     count += 1
#             ans.append(count)
#         return ans

#最优算法，时间复杂度；O(nlogn)
# from typing import List
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         sorted_nums = sorted(nums)
#         mapping = {}
#         for idx, val in enumerate(sorted_nums):
#             # 只记录数字【第一次出现】的下标
#             if val not in mapping:
#                 mapping[val] = idx
#         # 根据原数组查表得到答案
#         return [mapping[x] for x in nums]

