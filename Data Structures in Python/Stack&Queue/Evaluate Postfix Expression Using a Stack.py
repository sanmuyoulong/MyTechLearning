# Statement
# Given a string, exp, represents an arithmetic expression in a postfix notation. Evaluate exp and return the resulting integer value.

# The rules are given below:

# The valid operators are '+', '-', '*', and '/'.

# Each operand may be an integer or another expression.

# The division between two integers always truncates toward zero.

# There will not be any division by zero.

# The input represents a valid arithmetic expression in a postfix notation.

# The answer and all the intermediate calculations can be represented in a 32-bit integer.

from Stack import MyStack


def apply_operator(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 // num2  # Assuming integer division for simplicity

def evaluate_post_fix(exp):
    stack = MyStack()

    for char in exp:
        if char.isdigit():
            # Push numbers in stack
            stack.push(int(char))
        else:
            # Operator encountered
            # Pop top two numbers from stack
            right = stack.pop()
            left = stack.pop()
            # Apply operator to operands and push result back to stack
            result = apply_operator(char, left, right)
            stack.push(result)
    # Final result is at the top of the stack
    return stack.pop()


if __name__ == "__main__" :
    test_cases = ["921*-8-4+", "53+62/*35*+", "543-3*+", "82/3-31*+", "92+31*-"]

    i = 1
    for case in test_cases:
        print(i, ".\tExpression: ", case, sep="")
        result = evaluate_post_fix(case)
        print("\tResult: ", result)
        print("-"*100)
        i+=1