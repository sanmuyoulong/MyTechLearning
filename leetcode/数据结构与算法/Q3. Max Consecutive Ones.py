# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# from typing import List

# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
            
#         # 在头尾加上 0，方便计算区间
#         if nums[0] != 0:
#             nums.insert(0, 0)
#         if nums[-1] != 0:
#             nums.append(0)
        
#         index_list = []   # 记录所有 0 的位置
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 index_list.append(i)
        
#         # 计算每两个 0 之间的 1 的最大数量
#         max_count = 0
#         for k in range(len(index_list) - 1):
#             gap = index_list[k+1] - index_list[k] - 1   # 两个 0 之间 1 的个数
#             if gap > max_count:
#                 max_count = gap
        
#         return max_count


# # 测试
# examples = [[1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1]]
# for nums in examples:
#     solution = Solution()
#     answer = solution.findMaxConsecutiveOnes(nums[:])  # 复制一份避免修改原列表
#     print(f"输入: {nums} → 输出: {answer}")

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0  # 遇到0就重置计数器
        
        return max_count


# 测试
examples = [[1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1], [0]]

for nums in examples:
    solution = Solution()
    answer = solution.findMaxConsecutiveOnes(nums)
    print(f"输入: {nums} → 输出: {answer}")