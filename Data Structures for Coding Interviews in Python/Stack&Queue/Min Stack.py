from Stack import MyStack


class MinStack:
    # Constructor
    def __init__(self):
        self.min_stack = MyStack()
        self.main_stack = MyStack()

    # Pop from both stacks and return the popped value from the main_stack
    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()

    
    def push(self, value):
        self.main_stack.push(value) # Push new value value onto the main_stack
        if self.min_stack.is_empty() or self.min_stack.peek() > value :
            self.min_stack.push(value) # Push new value onto the min_stack
        else:
            self.min_stack.push(self.min_stack.peek()) # Again, push the top value onto min_stack
            
    # Returns minimum value from the min_stack in O(1) Time
    def min(self):
       return self.min_stack.peek()
 
# Driver code
def main():
    calls = [["MinStack","push()","push()","min()","pop()"],
             ["MinStack","push()","pop()","push()","min()"],
             ["MinStack","push()","push()","push()","push()", "pop()","min()"],
             ["MinStack","push()","min()","push()"],
             ["MinStack","push()","push()","min()","push()","min()"]
    
    ]

    inputs = [[None, 3, 7, None, 7],
              [None, -1, None, -4, None],
              [None, 100, 300, -200, -140, None, None],
              [None, 100000, None, -100000],
              [None, 54, 89, None, 45, None]
    ]

    for i in range(len(calls)):
        stack_obj = MinStack()

        print(i + 1, ".\t Starting operations:", sep="")

        # initialize a queue
        # loop over all the commands
        for j in range(len(calls[i])):
            if calls[i][j] == "push()":
                inputstr = "push" + \
                    "("+str(inputs[i][j])+")"
                print("\t\t", inputstr, sep="")
                stack_obj.push(inputs[i][j])
            elif calls[i][j] == "pop()":
                inputstr = "pop" + \
                    "("+")"
                print("\t\t", inputstr, "   returns ",
                      stack_obj.pop(), sep="")
            elif calls[i][j] == "min()":
                inputstr = "min" + \
                    "("+")"
                print("\t\t", inputstr, "   returns ",
                      stack_obj.min(), sep="")

        print("-" * 100)


if __name__ == "__main__":
    main()