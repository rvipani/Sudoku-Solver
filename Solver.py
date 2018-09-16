# Solver.py
"""
Solver contains all of the strategies and algorithms used to solve a Sudoku puzzle. Passing a Main.Grid to solve() will
solve the grid using all available strategies.
"""
import Main
import numpy as np

"""
Solver is used to perform all the actual solving of the puzzle. Solving loops repeatedly on the grid, using each of 
the possible solving algorithms each iteration until the board is solved.
"""
class Solver:

    def solve(self, grid):
        while self.isUnsolved(grid):
            self.nakedSingle(grid)
            grid.setPossibles()

    def isUnsolved(self, grid):
        # check for duplicates to see if there are errors
        for i in range(9):
            row = grid.getRow((i, 0))
            if self.hasDuplicates(row):
                    pass
            column = grid.getRow((0, i))
            if self.hasDuplicates(column):
                pass
            box = grid.getRow((i, 0))
            if self.hasDuplicates(box):
                pass
        # If no errors, check that every cell is filled.
        for i in range(9):
            for j in range(9):
                if grid.getCell((i, j)).getValue() == 0:
                    return False

        return True

    def hasDuplicates(self, mylist):
        while mylist.contains(0):
            mylist.remove(0)
        return len(mylist) != len(set(mylist))


    def nakedSingle(self, grid):
        for i in range(9):
            for j in range(9):
                cell = grid.getCell((i, j))
                if len(cell.possibleValues) == 1:
                    # print((i, j), cell.possibleValues[0])
                    cell.setValue(cell.possibleValues[0])

    def hiddenSingle(self, grid):
        for i in range(9):
            for j in range(9):
                cell = grid.getCell((i, j))


"""
DuplicateError error is used if the solver accidentally ever puts a number twice in the same row, column or box.
"""
class DuplicateError(Exception):
    def __init__(self, message):
        self.message = message
