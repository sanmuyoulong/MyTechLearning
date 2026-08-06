# Statement
# Given an unsorted list nums, find the sum of the maximum sum sublist. The maximum sum sublist is a list of contiguous elements in nums for which the sum of the elements is maximum.

# def find_max_sum_sublist(nums):
#     max_sum = float('-inf')
#     if len(nums) == 1:
#         return nums[0]
    
#     for i in range(1, len(nums)):
#         for j in range(0, len(nums) - i + 1):
#             sublist = nums[j:j+i]
#             sublist_sum = sum(sublist)
#             if sublist_sum > max_sum:
#                 max_sum = sublist_sum
#     return max_sum

# # Example usage:
# nums = [1]
# result = find_max_sum_sublist(nums)
# print("The sum of the maximum sum sublist is:", result)  # Output: 1

def find_max_sum_sublist(nums):
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]   # 初始化为第一个元素
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)   # 关键：要么从当前数重新开始，要么继续累加
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# 测试
test_cases = [
    [1],                    # 单元素
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],  # 经典例子
    [5, 4, -1, 7, 8],
    [-1, -2, -3, -4],
    [1, 2, 3, 4, 5]
]

for nums in test_cases:
    result = find_max_sum_sublist(nums)
    print(f"输入: {nums} → 最大子数组和: {result}")