from Stack import MyStack

def knows(matrix, x, y):
    # Returns True if x knows y, else returns False
    return matrix[x][y] == 1

def find_celebrity(matrix, n):
    stack = MyStack()
    celebrity = -1

    for i in range(n):
        stack.push(i)

    while not stack.is_empty():
        x = stack.pop()
        
        if stack.is_empty():
            celebrity = x
            break

        y = stack.pop()

        if knows(matrix, x, y):
            # x knows y, discard x and push y back in stack
            stack.push(y)
        else:
            # y is discarded, x is pushed back
            stack.push(x)

    # Verify the potential celebrity
    for j in range(n):
        # A celebrity knows no one, and everyone knows the celebrity
        if celebrity != j and (knows(matrix, celebrity, j) or not knows(matrix, j, celebrity)):
            return -1
    
    return celebrity

def main():
    matrixes = [
        [ # matrix 1
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [0, 0, 0, 0],
            [0, 1, 1, 0]
        ],
        [ # matrix 2
            [0, 1, 1, 0],
            [1, 0, 1, 1],
            [0, 0, 0, 1],
            [0, 1, 1, 0]
        ],
        [ # matrix 3
            [0, 0, 0, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 0]
        ],

        [ # matrix 4
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0]
        ],

        [ # matrix 5
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]

        ]        

    ]

    n = [4, 4, 4, 4, 5]

    for i in range(5):
        print(i+1, ".\tInput matrix:", matrixes[i])
        print("\tCelebrity:", find_celebrity(matrixes[i], n[i]))
        print("-"*100)

if __name__ == "__main__":
    main()