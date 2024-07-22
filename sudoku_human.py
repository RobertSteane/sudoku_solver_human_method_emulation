# create the sudoku grid
grid = []
grid.append([3, 0, 6, 5, 0, 8, 4, 0, 0])
grid.append([5, 2, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 8, 7, 0, 0, 0, 0, 3, 1])
grid.append([0, 0, 3, 0, 1, 0, 0, 8, 0])
grid.append([9, 0, 0, 8, 6, 3, 0, 0, 5])
grid.append([0, 5, 0, 0, 9, 0, 6, 0, 0])
grid.append([1, 3, 0, 0, 0, 0, 2, 5, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 7, 4])
grid.append([0, 0, 5, 2, 0, 6, 3, 0, 0])

# create a print function to nicely display the sudoku grid
def print_sudoku(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(board[i][j] if board[i][j] != 0 else '.', end=" ")
        print()

# print the initial sudoku grid
print_sudoku(grid)

# define a function to find every square in the same box as a chosen square
def box(i,j):
    rounded_i = (i // 3)*3
    i_box = [rounded_i, rounded_i + 1, rounded_i + 2]
    rounded_j = (j // 3) * 3
    j_box = [rounded_j, rounded_j + 1, rounded_j + 2]
    return i_box, j_box

# create a function to attempt to solve the sudoku
def solve(i, j):
    # options for numbers are 1-9
    options = list(range(1, 10))
    # check each row and column for numbers to eliminate possible option for a square
    for k in range(9):
        if j != k and grid[i][k] != 0:
            if grid[i][k] in options:
                options.remove(grid[i][k])
        if i != k and grid[k][j] != 0:
            if grid[k][j] in options:
                options.remove(grid[k][j])

    i_box, j_box = box(i, j)

    # check the box to eliminate possible options for a square
    for k in i_box:
        for l in j_box:
            if grid[k][l] != 0 and not (k == i and l == j):
                if grid[k][l] in options:
                    options.remove(grid[k][l])
    # If only one option remains, enter it in the grid
    if len(options) == 1:
        grid[i][j] = options[0]

# To improve this section, checks for boxes could be added in
    for row in range(9):
        for number in range(1, 10):
            if number not in grid[row]:
                row_placement_options = list(range(9))
                # remove any numbers in that row
                for m in range(9):
                    if grid[row][m] != 0:
                        row_placement_options.remove(m)
                columns_to_remove = []
                # check columns to remove possible placements of a number in that row
                for n in row_placement_options:
                    for o in range(9):
                        if grid[o][n] == number:
                            columns_to_remove.append(n)
                for k in columns_to_remove:
                    row_placement_options.remove(k)
                if len(row_placement_options) == 1:
                    grid[row][row_placement_options[0]] = number

    for column in range(9):
        for number in range(1,10):
            number_in_column = False
            # remove any numbers in that column
            for y in range(9):
                if number == grid[y][column]:
                    number_in_column = True
            if number_in_column is False:
                column_placement_options = list(range(9))
                for m in range(9):
                    if grid[m][column] != 0:
                        column_placement_options.remove(m)
                rows_to_remove = []
                # check rows to remove possible placements of a number in that column
                for n in column_placement_options:
                   for o in range(9):
                       if grid[n][o] == number and n in column_placement_options:
                           rows_to_remove.append(n)
                for k in rows_to_remove:
                    column_placement_options.remove(k)
                if len(column_placement_options) == 1:
                    grid[column_placement_options[0]][column] = number

# check to see if the grid contains any unfilled squares
def zero_check(grid):
    for row in grid:
        for cell in row:
            if cell == 0:
                return True
    return False
# while the sudoku is unfinished, keep running the solver algorithm
while zero_check(grid):
    for i in range(9):
       for j in range(9):
            if grid[i][j] == 0:
                solve(i,j)

# print the final solved sudoku
print("""
The solved sudoku is:
""")

print_sudoku(grid)
