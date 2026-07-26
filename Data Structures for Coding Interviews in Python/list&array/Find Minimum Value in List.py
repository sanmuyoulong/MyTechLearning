# Statement
# Given a list of integers, lst, find the minimum value from the list.
def find_minimum(lst):
    if not lst:
        return None  # Return None if the list is empty
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

cases = [
    [3, 1, 4, 1, 5, 9],
    [-7, -1, -3, -2],
    [10, 20, 30],
    [],
    [42]
]

for i, case in enumerate(cases):
    result = find_minimum(case)
    print(f"Case {i + 1}: {case} => Minimum: {result}")