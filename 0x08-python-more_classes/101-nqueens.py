#!/usr/bin/python3
import sys

def solve_nqueens(board, col, n):
    if col == n:
        result = []
        for i in range(n):
            row = board[i]
            result.append([row, i])
        print(result)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[col] = i
            res = solve_nqueens(board, col + 1, n) or res
            board[col] = -1

    return res

def is_safe(board, row, col, n):
    for i in range(col):
        if board[i] == row or \
           abs(board[i] - row) == abs(i - col):
            return False
    return True

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)

