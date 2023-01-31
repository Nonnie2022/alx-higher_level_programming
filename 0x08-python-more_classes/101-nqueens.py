#!/usr/bin/python3
import sys

def nqueens(N):
    def is_safe(board, row, col):
        # Check if it is safe to place a queen in the given row and col
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(board, row):
        # Solve the N queens problem
        if row == N:
            result.append(board[:])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)

    result = []
    board = [-1] * N
    solve(board, 0)
    return result

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print('N must be at least 4')
            sys.exit(1)
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    solutions = nqueens(N)
    for solution in solutions:
        print(solution)

