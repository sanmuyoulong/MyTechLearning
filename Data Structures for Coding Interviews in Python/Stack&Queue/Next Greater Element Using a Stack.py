# Statement
# Implement a next_greater_element() function that takes a list of integers, lst, as input and returns the next greater number for every element in the list.

# The next greater number for a number lst[i] is the first number to its right that is greater than lst[i]. If no such number exists, return -1 for this number.

from Stack import MyStack

def next_greater_element(lst):
    stack = MyStack()
    res = [-1] * len(lst)

    for i in reversed(range(len(lst))):
        # While stack has elements and the current element is greater 
        # than top element, pop all elements
        while not stack.is_empty() and stack.peek() <= lst[i]:
            stack.pop()

        # If the stack has an element, the top element will be 
        # greater than ith element
        if not stack.is_empty():
            res[i] = stack.peek()
        stack.push(lst[i])
        
    return res

def main():
    inputs = [[4, 6, 3, 2, 8, 1, 9, 9, 9],
              [33, 20, 105, 88],
              [12, 5, 44, 56, 46, 78],
              [1, 2, 3, 4, 5],
              [150, 125, 100, 75, 50, 25, 0]]

    for i in range(len(inputs)):
        print(i + 1, ".\tList: ", inputs[i], sep="")
        print("\n\tResult: ", next_greater_element(inputs[i]))
        print("-" * 100)

if __name__ == "__main__":
    main()