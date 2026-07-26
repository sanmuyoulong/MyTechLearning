class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + nums
        return ans

nums = [1, 2, 3]
solution = Solution()
result = solution.getConcatenation(nums)
print(result)