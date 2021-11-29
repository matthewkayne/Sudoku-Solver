# Define Sudoku board
board = [[6,4,0,0,0,0,0,0,2],
         [9,0,0,0,5,0,7,0,0],
         [0,8,0,0,0,3,0,0,0],
         [0,0,3,0,6,0,1,0,0],
         [0,0,0,3,0,8,0,0,0],
         [0,0,4,0,7,0,5,0,0],
         [0,0,0,8,0,0,0,7,0],
         [0,0,7,0,2,0,0,0,9],
         [5,0,0,0,0,0,0,6,4]]

# Checks if a number fits the constraints
def possible(y,x,n):
    global board
    for i in range(9):
        if board[y][i] == n:
            return False
    for j in range(9):      
        if board[j][x] == n:
            return False
    xbox = (x//3)*3
    ybox = (y//3)*3
    for i in range(3):
        for j in range(3):
            if board[ybox+i][xbox+j] == n:
                return False
    return True

# Solves the board
def solve():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        board[y][x] = n
                        # Recursion
                        solve()
                        # Backtracking
                        board[y][x] = 0
                return None
    for i in range(9):
        print(board[i])         
solve()    