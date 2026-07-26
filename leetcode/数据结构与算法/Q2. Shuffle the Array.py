# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
    
example_nums = [([1, 2, 3, 4, 5, 6], 3), ([1, 1, 2, 2], 2), ([1, 2], 1)]

for nums, n in example_nums:
    solution = Solution()
    result = solution.shuffle(nums, n)
    print(result)