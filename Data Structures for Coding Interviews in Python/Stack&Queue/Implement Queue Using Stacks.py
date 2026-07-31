# Statement
# Design a queue data structure using only two stacks and implement the following functions:

# enqueue(int x): Inserts a value to the back of the queue.
# dequeue(): Removes and returns the value from the front of the queue.

from Stack import MyStack


class NewQueue:
    # Can use the size from the argument to create the stack
    def __init__(self):
        self.main_stack = MyStack()
        self.temp_stack = MyStack()

    # Inserts element in the queue
    def enqueue(self, value):
        # Push the value into main_stack in O(1)
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            self.main_stack.push(value)
        else:
            while not self.main_stack.is_empty():
                self.temp_stack.push(self.main_stack.pop())
            # Inserting the value in the queue
            self.main_stack.push(value)
            while not self.temp_stack.is_empty():
                self.main_stack.push(self.temp_stack.pop())

    # Removes element from queue
    def dequeue(self):
        # If stack empty then return None
        if self.main_stack.is_empty():
            return None
        value = self.main_stack.pop()
        return value

from Stack import MyStack


# class NewQueue:

#     def __init__(self):
#         self.main_stack = MyStack()
#         self.temp_stack = MyStack()

#     # Inserts element in the queue
#     def enqueue(self, value):
#         # Push the value into main_stack in O(1)
#         self.main_stack.push(value)

#     # Removes element from the queue
#     def dequeue(self):
#         # If both stacks are empty, end the operation
#         if not self.temp_stack.is_empty():
#             front = self.temp_stack.pop()
#             return front
#         if self.temp_stack.is_empty() and self.main_stack.is_empty():
#             return None
#         # Transfer all elements to temp_stack
#         while not self.main_stack.is_empty():
#             self.temp_stack.push(self.main_stack.pop())
#         # Pop the first value. This is the oldest element in the queue
#         front = self.temp_stack.pop()
#         return front



# Driver code
def main():
    calls = [["NewQueue","enqueue()","enqueue()","enqueue()","dequeue()"],
             ["NewQueue","enqueue()","dequeue()","enqueue()","dequeue()"],
             ["NewQueue","enqueue()","enqueue()","dequeue()","dequeue()"],
             ["NewQueue","enqueue()","enqueue()","dequeue()","enqueue()"],
             ["NewQueue","enqueue()","dequeue()","enqueue()","enqueue()"]
    
    ]

    inputs = [[None, 3, 4, 5, None],
              [None, -1, None, -4, None],
              [None, 200, 700, None, None],
              [None, -100, -100, None, -100],
              [None, 100000, None, -100000, 4000]
    ]

    for i in range(len(calls)):
        queue_obj = NewQueue()

        print(i + 1, ".\t Starting operations:", sep="")

        # Initialize a queue
        # Loop over all the commands
        for j in range(len(calls[i])):
            if calls[i][j] == "enqueue()":
                inputstr = "enqueue" + \
                    "("+str(inputs[i][j])+")"
                print("\t\t", inputstr, sep="")
                queue_obj.enqueue(inputs[i][j])
            if calls[i][j] == "dequeue()":
                inputstr = "dequeue" + \
                    "("+")"
                print("\t\t", inputstr, "   returns ",
                      queue_obj.dequeue(), sep="")

        print("-" * 100)


if __name__ == "__main__":
    main()