# Statement
# Given a number n, generate a list of binary numbers from 1 to n in the form of a string using a queue.

from Queue import MyQueue

def find_bin(n):
    result = []
    queue = MyQueue()

    queue.enqueue("1")

    for i in range(n):
        result.append(queue.dequeue())

        s1 = result[i] + "0"
        s2 = result[i] + "1"

        queue.enqueue(s1)
        queue.enqueue(s2)

    return result

def main():
    inputs = [5, 10, 15, 20]

    for n in inputs:
        print(f"Binary numbers from 1 to {n}: {find_bin(n)}")

if __name__ == "__main__":
    main()