# def rearrange_list(nums):
#     if not nums:
#         return []
#     nums.sort(reverse = True)
#     ralist = [0] * (2 * len(nums))
#     for i in range(len(nums)):
#         ralist[2 * i] = nums[i]
#     for i in range(len(nums)):
#         ralist[2 * i + 1] = nums[-i - 1]

#     ralist = ralist[:len(nums):]
#     return ralist

# # Test cases
# cases = [
#     [1, 2, 3, 4, 5],
#     [10, 20, 30, 40, 50],
#     [5, 4, 3, 2, 1],
#     [1, 3, 5, 7, 9],
#     [2, 4, 6, 8, 10],
#     []
# ]

# for i, case in enumerate(cases):
#     result = rearrange_list(case)
#     print(f"Case {i + 1}: {case} => Result: {result}")


def rearrange_list(nums):
    if (len(nums) == 0):
        return []

    # Initialize pointers to the start and end of the list
    max_idx = len(nums) - 1
    min_idx = 0
    # Initialize a variable larger than any element in the list to use for encoding
    max_elem = nums[len(nums) - 1] + 1

    # Encoding phase
    for i in range(len(nums)):
        if i % 2 == 0:  # Encoding at even indexes
            nums[i] += (nums[max_idx] % max_elem) * max_elem
            max_idx -= 1
        else:  # Encoding at odd indexes
            nums[i] += (nums[min_idx] % max_elem) * max_elem
            min_idx += 1

    # Decoding phase
    for i in range(len(nums)):
        nums[i] = nums[i] // max_elem

    return nums


def main():
    input_list = [[1, 2, 3, 4, 5, 6, 7, 8],
				  [11, 22, 33, 44, 55, 66, 77, 88],
				  [1, 2, 4, 8, 16, 32, 64, 128, 512, 1024],
				  [3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13],
				  [100, 233, 544, 753, 864, 935, 1933, 2342]]

    for i in range(len(input_list)):
        print(i + 1, ".\tOriginal list: ", input_list[i], sep='')
        print("\tRearranged list: ", rearrange_list(input_list[i]), sep='')
        print("-" * 100)


if __name__ == '__main__':
    main()
    