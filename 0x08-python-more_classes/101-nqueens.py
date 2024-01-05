import sys

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_solution(board, n):
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q" if board[row] == col else "."
        print(line)
    print()

def solve_nqueens(board, row, n):
    if row == n:
        print_solution(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            board[row] = -1

def nqueens(n):
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)

