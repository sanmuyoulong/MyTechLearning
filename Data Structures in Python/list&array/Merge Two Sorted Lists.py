# Statement
# Given two integer lists, nums1 and nums2, of size m and n, respectively, sorted in nondecreasing order. Merge nums1 and nums2 into a single list sorted in nondecreasing order.

def merge_lists(nums1, nums2):
    merge_list = []
    i, j = 0, 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merge_list.append(nums1[i])
            i += 1
        else:
            merge_list.append(nums2[j])
            j += 1
    
    # 把剩余元素全部加入
    merge_list.extend(nums1[i:])
    merge_list.extend(nums2[j:])
    
    return merge_list

test_cases = [
    ([1, 3, 5], [2, 4, 6]), 
    ([1, 2, 3], [4, 5, 6]), 
    ([1, 3, 5], []), 
    ([], [2, 4, 6]), 
    ([], []), 
    ([1, 2, 2], [2, 3, 4]), 
    ([1], [0]),
]

for nums1, nums2 in test_cases:
    result = merge_lists(nums1, nums2)
    print(f"输入: {nums1}, {nums2} → 输出: {result}")