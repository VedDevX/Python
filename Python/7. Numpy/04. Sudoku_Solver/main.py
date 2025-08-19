import numpy as np

# Sample Sudoku board (0 = empty cell)
board = np.array([
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
])

# Print the Sudoku board neatly
def print_board(b):
    for i in range(9):
        row_str = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            if b[i][j] == 0:
                row_str += ". "
            else:
                row_str += str(b[i][j]) + " "
        print(row_str)
        if i % 3 == 2 and i != 8:
            print("- "*11)

# Check if placing num at (row, col) is valid
def is_valid(b, num, row, col):
    # Check row
    if num in b[row]:
        return False
    # Check column
    if num in b[:, col]:
        return False
    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if b[start_row + i][start_col + j] == num:
                return False
    return True

# Find the first empty cell
def find_empty(b):
    for i in range(9):
        for j in range(9):
            if b[i][j] == 0:
                return i, j
    return None

# Solve Sudoku using backtracking
def solve(b):
    empty_cell = find_empty(b)
    if not empty_cell:
        return True  # board solved
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(b, num, row, col):
            b[row][col] = num
            if solve(b):
                return True
            b[row][col] = 0  # backtrack
    return False

# Menu
def show_menu():
    print("\n🧩 Sudoku Solver Menu")
    print("1. Show Board")
    print("2. Solve Sudoku")
    print("3. Exit")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        print("\n📋 Current Sudoku Board:")
        print_board(board)
    
    elif choice == "2":
        if solve(board):
            print("\n✅ Sudoku Solved!")
            print_board(board)
        else:
            print("❌ No solution exists.")
    
    elif choice == "3":
        print("👋 Goodbye!")
        break
    
    else:
        print("❌ Invalid choice! Enter 1-3.")
