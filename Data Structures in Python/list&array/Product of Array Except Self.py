# Statement
# You’re given an integer array, nums. Return a resultant array product so that product[i] is equal to the product of all the elements of nums except nums[i].

# Write an algorithm that runs in O(n) time without using the division operation.
def find_product(nums):
    n = len(nums)
    res = [1] * n
    pre = 1
    # 前缀积
    for i in range(n):
        res[i] = pre
        pre *= nums[i]
    suf = 1
    # 后缀积
    for i in range(n-1, -1, -1):
        res[i] *= suf
        suf *= nums[i]
    return res

example_nums = [1, 2, 3, 4]
result = find_product(example_nums)
print(result)  # Output: [24, 12, 8, 6]