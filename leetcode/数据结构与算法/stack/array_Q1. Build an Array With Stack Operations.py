# You are given an integer array target and an integer n.

# You have an empty stack with the two following operations:

# "Push": pushes an integer to the top of the stack.
# "Pop": removes the integer on the top of the stack.
# You also have a stream of the integers in the range [1, n].

# Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target. You should follow the following rules:

# If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.
# If the stack is not empty, pop the integer at the top of the stack.
# If, at any moment, the elements in the stack (from the bottom to the top) are equal to target, do not read new integers from the stream and do not do more operations on the stack.
# Return the stack operations needed to build target following the mentioned rules. If there are multiple valid answers, return any of them.

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        current = 1
        for num in target:
            while current < num:
                operations.append("Push")
                operations.append("Pop")
                current += 1
            operations.append("Push")
            current += 1
        return operations

def main():
    solution = Solution()
    target_list = [
        [1, 3, 5],
        [1, 2, 3],
        [1, 2],
        [2, 3, 4],
        [1, 3, 4, 5]
    ]

    n_list = [5, 3, 4, 4, 5]

    for i in range(len(target_list)):
        target = target_list[i]
        n = n_list[i]
        result = solution.buildArray(target, n)
        print(f"Target: {target}, n: {n} => Operations: {result}")

if __name__ == "__main__":
    main()