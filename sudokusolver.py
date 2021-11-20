import time

def sudoku_solve(board):
    #Find first empty spot and return if no empty spaces exist
    try:
        # convert 2d list to 1d, get index of 0 and convert index back to 2d
        x, y = divmod(sum(board, []).index(0), 9)
    except ValueError:
        return board

    # Find possible values for empty spot
    row_nums = set(board[x])
    col_nums = set([row[y] for row in board])

    col_begin = y - y % 3
    col_end = row_begin + 3
    row_begin = x - x % 3 
    row_end = column_begin + 3
    block_nums = set(sum([row[col_begin: col_end] for row in board[row_begin: row_end]], []))

    options = set(range(1, 10)) - (row_nums | col_nums | block_nums)

    # Solve further on board with value applied
    for option in options:
        try:
            board[x][y] = option
            return sudoku_solve(board)
        except AttributeError:
            board[x][y] = 0
    raise AttributeError


board0 = [[1, 0, 0, 0, 0, 0, 0, 6, 0],
          [0, 0, 0, 0, 7, 5, 0, 3, 0],
          [0, 4, 8, 0, 9, 0, 1, 0, 0],
          [0, 0, 0, 3, 0, 0, 0, 0, 0],
          [3, 0, 0, 0, 1, 0, 0, 0, 9],
          [0, 0, 0, 0, 0, 8, 0, 0, 0],
          [0, 0, 1, 0, 2, 0, 5, 7, 0],
          [0, 8, 0, 7, 3, 0, 0, 0, 0],
          [0, 9, 0, 0, 0, 0, 0, 0, 4]]

board1 = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
          [6, 0, 0, 0, 7, 5, 0, 0, 9],
          [0, 0, 0, 6, 0, 1, 0, 7, 8],
          [0, 0, 7, 0, 4, 0, 2, 6, 0],
          [0, 0, 1, 0, 5, 0, 9, 3, 0],
          [9, 0, 4, 0, 6, 0, 0, 0, 5],
          [0, 7, 0, 3, 0, 0, 0, 1, 2],
          [1, 2, 0, 0, 0, 7, 4, 0, 0],
          [0, 4, 9, 2, 0, 6, 0, 0, 7]]


for r in sudoku_solve(board1):
    print(r)
print("\n")

print(time.perf_counter())
