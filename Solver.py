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
            row = grid.cellsToVals(grid.getRow((i, 0)))
            if self.hasDuplicates(row):
                message = "Row " + str(i) + " contains a duplicate"
                raise DuplicateError(message)
            column = grid.cellsToVals(grid.getColumn((0, i)))
            if self.hasDuplicates(column):
                message = "Column " + str(i) + " contains a duplicate"
                raise DuplicateError(message)
            box = grid.cellsToVals(grid.getBox((int(i/3), i % 3)))
            if self.hasDuplicates(box):
                message = "Box " + str(i) + " contains a duplicate"
                raise DuplicateError(message)

        # If no errors, check that every cell is filled.
        for i in range(9):
            for j in range(9):
                if grid.getCell((i, j)).getValue() == 0:
                    return True
        return False

    def hasDuplicates(self, mylist):
        mylist = mylist
        while 0 in mylist:
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
