#
# Sudoku Solver (5/16/2023)
# Isaac B. Ernst
#

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# prints the puzzle and solution...
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('=========================')
        for j in range(len(bo[i])):
            if j % 3 == 0 and j != 0:
                print(' | ', end=' ')
            if j == 8:
                print(bo[i][j])
            elif bo[i][j] == 0:
                print('_', end=' ')
            else:
                print(bo[i][j], end=' ')


# finds empty spaces in the puzzle...
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return i, j
    return None


# checks if the number is valid (obeys game rules)...
def check_valid(bo, num, row, col):
    # Check the row...
    for i in range(len(bo)):
        if bo[row][i] == num and i != col:
            return False
    # Check the column...
    for i in range(len(bo[0])):
        if bo[i][col] == num and i != row:
            return False
    # Check the box...
    box_x = (col // 3) * 3
    box_y = (row // 3) * 3
    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if bo[i][j] == num and (i, j) != (row, col):
                return False
    return True


# uses the above functions to solve...
def solve_puzzle(bo):
    if not find_empty(bo):
        return True
    else:
        row, col = find_empty(bo)
        for i in range(1, 10):
            if check_valid(bo, i, row, col):
                bo[row][col] = i
                if solve_puzzle(bo):
                    return True
                bo[row][col] = 0
    return False


print('Sudoku Puzzle:')
print_board(board)
solve_puzzle(board)
print('\nPuzzle\'s solution:')
print_board(board)
