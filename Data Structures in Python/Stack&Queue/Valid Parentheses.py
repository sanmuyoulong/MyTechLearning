# Statement
# Given a string, exp, which may consist of opening and closing parentheses. Your task is to check whether or not the string contains valid parenthesization.

# The conditions to validate are as follows:

# Every opening parenthesis should be closed by the same kind of parenthesis. Therefore, {) and [(]) strings are invalid.

# Every opening parenthesis must be closed in the correct order. Therefore, )( and ()(() are invalid.

from Stack import MyStack


def is_balanced(exp):
    stack = MyStack()

    for char in exp:
        if char in ['(', '{', '[']:
            stack.push(char)
        elif char in [')', '}', ']']:
            if stack.is_empty():
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                return False

    # If the stack is empty, all parentheses were matched
    return stack.is_empty()