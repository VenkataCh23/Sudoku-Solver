import tkinter as tk
from tkinter import messagebox

def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

def is_safe(grid, row, col, num):
    if num in grid[row]:
        return False
    if num in [grid[i][col] for i in range(9)]:
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def get_grid():
    grid = []
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            row.append(int(val) if val else 0)
        grid.append(row)
    return grid

def set_grid(grid):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            if grid[i][j] != 0:
                entries[i][j].insert(0, str(grid[i][j]))

def solve():
    grid = get_grid()
    if solve_sudoku(grid):
        set_grid(grid)
    else:
        messagebox.showinfo("Sudoku Solver", "No solution exists")

def clear():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)

root = tk.Tk()
root.title("Sudoku Solver")

entries = [[tk.Entry(root, width=2, font=('Arial', 18), justify='center') for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        entries[i][j].grid(row=i, column=j, padx=5, pady=5)

solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.grid(row=9, column=0, columnspan=5)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=9, column=5, columnspan=4)

