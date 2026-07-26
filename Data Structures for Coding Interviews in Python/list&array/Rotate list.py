# Statement
# You are given an integer list, nums, and a non-negative integer k. Your task is to rotate the list to the right by k steps.

# In a right rotation, the last element moves to the front, and all other elements shift one position to the right.

def right_rotate(nums, k):
    n = len(nums)
    if n == 0:
        return nums  # Return the original list if it's empty
    k = k % n  # Handle cases where k is greater than the length of the list
    return nums[-k:] + nums[:-k]  # Rotate the list

cases = [
    ([1, 2, 3, 4, 5], 2),
    ([1, 2, 3, 4, 5], 0),
    ([1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 4, 5], 7)  # k > len(nums)
]

for i, (case, k) in enumerate(cases):
    result = right_rotate(case, k)
    print(f"Case {i + 1}: {case} rotated by {k} => Result: {result}")