#Solver.py
"""
Solver contains all of the strategies and algorithms used to solve a Sudoku puzzle. Passing a Main.Grid to solve() will
solve the grid using all available strategies.
"""
import Main
import numpy as np


class Solver:

    def solve(self, grid):
        pass

    def isUnsolved(self, grid):
        pass

    def lastDigit(self, grid):
        for i in range(9):
            for j in range(9):
                cell = grid.getCell((i, j))
                if len(cell.possibleValues) == 1:
                    #print((i, j), cell.possibleValues[0])
                    cell.setValue(cell.possibleValues[0])
