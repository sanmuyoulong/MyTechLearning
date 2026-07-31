# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
    # 第一次遍历：把出现过的数字对应的下标位置标记为负数
        for num in nums:
            index = abs(num) - 1          # 数字 k 对应下标 k-1
            if nums[index] > 0:
                nums[index] = -nums[index]
    
    # 第二次遍历：下标位置仍为正数的，说明该数字从未出现
        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)
    
        return result

def main():
    solution = Solution()
    nums = [4,3,2,7,8,2,3,1]
    result = solution.findDisappearedNumbers(nums)
    print(result)  # Output: [5, 6]

if __name__ == "__main__":
    main()