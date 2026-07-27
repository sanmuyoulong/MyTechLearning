# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()  # 排序数组
        test_nums = []
        for x in nums:
            if x not in test_nums:
                test_nums.append(x)
            else:
                dup_num = x

        for i in range(len(nums)):
            if i + 1 not in test_nums:
                miss_num = i + 1
        return [dup_num, miss_num]

def main():
    solution = Solution()
    inputs = [
        [1, 2, 2, 4],
        [1, 1],
        [2, 2],
        [3, 2, 3, 4, 6, 5],
        [1, 5, 3, 2, 2, 7, 6, 4]
    ]

    for nums in inputs:
        result = solution.findErrorNums(nums)
        print(f"Input: {nums} → Output: {result}")

if __name__ == "__main__":
    main()   