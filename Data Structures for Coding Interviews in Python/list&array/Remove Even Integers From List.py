# Statement
# Given a list of integers, lst, remove all the even integers from the list.

# 1<=lst.length<=10^3
# -10^5<=lst[i]<=10^5

def remove_even(lst):
    return [x for x in lst if x % 2 != 0]

# 测试用例
test_cases = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [2, 4, 6, 8, 10],
    [1, 3, 5, 7, 9],
    [-4, -3, -2, -1, 0, 1, 2],
    []
]

for lst in test_cases:
    result = remove_even(lst)
    print(f"输入: {lst} → 输出: {result}")