# Statement
# Given a list nums, find the first nonrepeating integer in it.
def first_non_repeating(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for num in nums:
        if count[num] == 1:
            return num
    return None  # Return None if no non-repeating element is found

cases = [
    [4, 5, 1, 2, 0, 4],
    [1, 2, 3, 4, 5],
    [1, 1, 2, 2, 3, 3],
    [1],
    []
]

for i, case in enumerate(cases):
    result = first_non_repeating(case)
    print(f"Case {i + 1}: {case} => First non-repeating: {result}")