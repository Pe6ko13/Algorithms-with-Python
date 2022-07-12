def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def can_place_queen(row, col, rows, cols, left_diagonal, right_diagonal):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in left_diagonal:
        return False
    if (row + col) in right_diagonal:
        return False
    return True

def set_queen(row, col, board, rows, cols, left_diagonal, right_diagonal):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left_diagonal.add(row-col)
    right_diagonal.add(row+col)

def remove_queen(row, col, board, rows, cols, left_diagonal, right_diagonal):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left_diagonal.remove(row - col)
    right_diagonal.remove(row + col)

def put_queens(row, board, rows, cols, left_diagonal, right_diagonal):
    if row == 8:
        print_board(board)
        return


    for col in range(8):
        if can_place_queen(row, col, rows, cols, left_diagonal, right_diagonal):
            set_queen(row, col, board, rows, cols, left_diagonal, right_diagonal)
            put_queens(row + 1, board, rows, cols, left_diagonal, right_diagonal)
            remove_queen(row, col, board, rows, cols, left_diagonal, right_diagonal)

n = 8
board = []
[board.append(['-'] * n) for _ in range(8)]

put_queens(0, board, set(), set(), set(), set(),)