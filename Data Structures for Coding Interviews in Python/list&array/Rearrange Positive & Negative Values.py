# Statement
# Implement a function that rearranges elements in a list so that all negative elements appear to the left and all positive elements (including zero) appear to the right. It’s important to note that maintaining the original sorted order of the input list is not required for this task.

def rearrange(nums):
    return [x for x in nums if x < 0] + [x for x in nums if x >= 0]

# Test cases
cases = [
    [-1, 2, -3, 4, 5],
    [1, 2, 3, 4, 5],
    [-1, -2, -3, -4, -5],
    [0, -1, 2, -3, 4],
    []
]

for i, case in enumerate(cases):
    result = rearrange(case)
    print(f"Case {i + 1}: {case} => Result: {result}")