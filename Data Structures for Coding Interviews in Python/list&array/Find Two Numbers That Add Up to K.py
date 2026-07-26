# Statement
# Given a list of integers, nums, and an integer target, k, find two numbers in the list that sum up to the target k.

# There is exactly one solution for each input, and each element of the list can only be used once in the solution. The order of the returned elements does not matter.

def find_sum(nums, k):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):   # 避免重复使用同一个元素
            if nums[i] + nums[j] == k:
                return [nums[i], nums[j]]
    
    return 'There is no solution'

example_nums = [2, 7, 11, 15]
example_k = 9
result = find_sum(example_nums, example_k)
print(result)  # Output: [2, 7]