# Statement
# Given a list of integers, nums, find the second maximum value from the list.

def find_second_maximum(nums):
    if len(nums) < 2:
        return None  # Return None if there are less than 2 unique elements
    unique_nums = list(set(nums))  # Remove duplicates
    unique_nums.sort(reverse=True)  # Sort in descending order
    return unique_nums[1]  # Return the second maximum value

cases = [
    [4, 5, 1, 2, 0, 4],
    [1, 2, 3, 4, 5],
    [1, 1, 2, 2, 3, 3],
    [1],
    []
]
for i, case in enumerate(cases):
    result = find_second_maximum(case)
    print(f"Case {i + 1}: {case} => Second maximum: {result}")