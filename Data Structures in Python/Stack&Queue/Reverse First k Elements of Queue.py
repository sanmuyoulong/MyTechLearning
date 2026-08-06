# Statement
# Given a queue and a number k, reverse the order of the first k elements in queue. If k is less than 0, or if k exceeds queue size, or if queue is empty, return NULL. Otherwise, return the modified queue.

from Queue import MyQueue
from Stack import MyStack


def reverse_k_elements(queue, k):
    if k < 0 or k > queue.size() or queue.is_empty():
        return None

    stack = MyStack()
    for _ in range(k):
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())

    size = queue.size()
    for i in range(size - k):
        queue.enqueue(queue.dequeue())

    # Replace this placeholder return statement with your code
    return queue

if __name__ == "__main__":
    test_queue = [
        [1,2,3,4,5,6,7,8,9,10],
        [-2,1,-5,45,6,3,-9],
        [1,2,5,0,7,4,23],
        [7,3,5,6,8,12],
        [5,67,43,23,12,56,78,98,6,21,9]
    ]

    for i in range(len(test_queue)):
        queue_obj = MyQueue()
        for j in range(len(test_queue[i])):
            queue_obj.enqueue(test_queue[i][j])

        print("Original Queue: " + str(queue_obj.print_list()))
        k = int(input("Enter the value of k: "))
        modified_queue = reverse_k_elements(queue_obj, k)
        if modified_queue is None:
            print("Invalid value of k. Queue remains unchanged.")
        else:
            print("Modified Queue: " + str(modified_queue.print_list()))