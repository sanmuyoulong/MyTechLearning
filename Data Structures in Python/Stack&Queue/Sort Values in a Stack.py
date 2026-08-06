# Statement
# Given a stack of integers, stack, sort its elements in ascending order. In the resulting stack, the smallest element should be at the top.

from Stack import MyStack


def sort_stack(stack):
    temp_stack = MyStack()

    while not stack.is_empty():
        # Pop the top element from the original stack
        current = stack.pop()

        # While temporary stack is not empty and top of temp_stack is greater than current
        while not temp_stack.is_empty() and temp_stack.peek() > current:
            # Pop from temp_stack and push it back to the original stack
            stack.push(temp_stack.pop())

        # Push the current element onto the temporary stack
        temp_stack.push(current)

    # Replace this placeholder return statement with your code
    return temp_stack

def main():
    inputs = [
        [3, 1, 4, 1, 5, 9, 2, 6],
        [2, 7, 1, 8, 2, 8, 1, 8],
        [5, 3, 5, 8, 9, 7, 9, 3],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4,4,2,2,1,1]
    ]

    for input_list in inputs:
        stack = MyStack()
        for item in input_list:
            stack.push(item)

        sorted_stack = sort_stack(stack)

        # Print the sorted stack
        sorted_elements = []
        while not sorted_stack.is_empty():
            sorted_elements.append(sorted_stack.pop())
        print(sorted_elements)

if __name__ == "__main__":
    main()