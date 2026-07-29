class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.list_size = size
        self.ans = [0] * size
        self.top1 = -1
        self.top2 = self.list_size

    # Insert Value in First Stack
    def push1(self, value):
        if self.top1 + 1 == self.top2:
            return 'Stack Overflow'
        self.top1 += 1
        self.ans[self.top1] = value

    # Insert Value in Second Stack
    def push2(self, value):
        if self.top2 - 1 == self.top1:
            return 'Stack Overflow'
        self.top2 -= 1
        self.ans[self.top2] = value

    # Return and remove top Value from First Stack
    def pop1(self):
        if self.top1 == -1:
            return 'Stack Underflow'
        self.top1 -= 1
        return self.ans[self.top1 + 1]

    # Return and remove top Value from Second Stack
    def pop2(self):
        if self.top2 == self.list_size:
            return 'Stack Underflow'
        self.top2 += 1
        return self.ans[self.top2 - 1]

def main():
    stack_obj = TwoStacks(10)

    print("Pushing elements into the first stack")
    for i in range(5):  
        print(i)
        stack_obj.push1(i)

    print("Pushing elements into the second stack")
    for i in range(5, 10):  
        print(i)
        stack_obj.push2(i)

    print("Popping elements from the first stack")
    for x in range(5):  
        print(stack_obj.pop1())

    print("Popping elements from the second stack")
    for x in range(5):  
        print(stack_obj.pop2())

if __name__ == "__main__":
    main()