# Solver.py
"""
Solver contains all of the strategies and algorithms used to solve a Sudoku puzzle. Passing a Main.Grid to solve() will
solve the grid using all available strategies.
"""
import Main
import numpy as np
import itertools

"""
Solver is used to perform all the actual solving of the puzzle. Solving loops repeatedly on the grid, using each of 
the possible solving algorithms each iteration until the board is solved.
"""
class Solver:

    # Strategies are included in solve when they are completed
    # Counter exists in case the puzzle is not solvable and needs to quit
    def solve(self, grid):
        counter = 0
        while self.isUnsolved(grid) and counter < 100:
            self.nakedSingle(grid)
            self.hiddenSingle(grid)
            self.lockedCandidate(grid)
            self.hiddenSubset(grid)
            self.nakedSubset(grid)
            counter += 1
            # if Main.DEBUG is True:
                # grid.print()
        if self.isUnsolved(grid):
            print("Unable to solve this puzzle")
        else:
            print("Done")

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
            box = grid.cellsToVals(grid.getBox((int(i/3) * 3, (i % 3) * 3)))
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
                    grid.setCell((i, j), (cell.possibleValues[0]))
        if Main.DEBUG is True:
            grid.print()

    def hiddenSingle(self, grid):
        for i in range(9):
            for j in range(9):
                cell = grid.getCell((i, j))
                possibleValues = cell.possibleValues
                for value in possibleValues:
                    # For each of the possible values of the cell, we want to check if that value only exists once
                    # in that house

                    # Flag represents weather or not another cell also contains that value
                    # Check row
                    flag = False
                    house = grid.getRow(cell.location)
                    for othercell in house:
                        if othercell != cell:
                            otherPVs = othercell.possibleValues
                            if value in otherPVs:
                                flag = True
                                break
                    if flag is False:
                        grid.setCell((i, j), value)
                        break

                    # Check column
                    flag = False
                    house = grid.getColumn(cell.location)
                    for othercell in house:
                        if othercell != cell:
                            otherPVs = othercell.possibleValues
                            if value in otherPVs:
                                flag = True
                                break
                    if flag is False:
                        grid.setCell((i, j), value)
                        break

                    # Check box
                    flag = False
                    house = grid.getBox(cell.location)
                    for othercell in house:
                        if othercell != cell:
                            otherPVs = othercell.possibleValues
                            if value in otherPVs:
                                flag = True
                                break
                    if flag is False:
                        grid.setCell((i, j), value)
                        break
        if Main.DEBUG is True:
            grid.print()

    def lockedCandidate(self, grid):
        self.pointing(grid)
        self.claiming(grid)

    def pointing(self, grid):
        # Handle Pointing first by iterating through box, then check each digit 1-9 in each box to see if the box
        # has any pointing
        for i in range(9):
            box = grid.getBox((int(i / 3) * 3, (i % 3) * 3))
            for digit in range(1, 10):
                temp = []
                for cell in box:
                    if digit in cell.possibleValues:
                        temp.append(cell)
                if len(temp) == 0:
                    continue

                # Check if each cell with that digit is in the same row
                if self.inSameRow(temp):
                    # Remove that digit from the entire row.
                    row = grid.getRow(temp[0].location)
                    for cell in row:
                        pvs = cell.possibleValues
                        if cell not in box and digit in pvs:
                            pvs.remove(digit)

                # Check if each cell with that digit is in the same column
                elif self.inSameCol(temp):
                    # Remove that digit from the entire row.
                    column = grid.getColumn(temp[0].location)
                    for cell in column:
                        pvs = cell.possibleValues
                        if cell not in box and digit in pvs:
                            pvs.remove(digit)
        if Main.DEBUG is True:
            grid.print()

    def claiming(self, grid):
        # Handle Claiming checking rows first
        for i in range(9):
            house = grid.getRow((i, 0))
            for digit in range(1, 10):
                temp = []
                for cell in house:
                    if digit in cell.possibleValues:
                        temp.append(cell)
                if len(temp) == 0:
                    continue
                if self.inSameBox(temp):
                    # Remove that digit from the entire Box.
                    box = grid.getBox(temp[0].location)
                    for cell in box:
                        pvs = cell.possibleValues
                        if cell not in house and digit in pvs:
                            pvs.remove(digit)
        # Handle Claiming checking columns next
        for i in range(9):
            house = grid.getColumn((0, i))
            for digit in range(1, 10):
                temp = []
                for cell in house:
                    if digit in cell.possibleValues:
                        temp.append(cell)
                if len(temp) == 0:
                    continue
                if self.inSameBox(temp):
                    # Remove that digit from the entire Box.
                    box = grid.getBox(temp[0].location)
                    for cell in box:
                        pvs = cell.possibleValues
                        if cell not in house and digit in pvs:
                            pvs.remove(digit)
        if Main.DEBUG is True:
            grid.print()

    def hiddenSubset(self, grid):
        for size in range(2, 5):
            # Iterate through Rows
            for i in range(9):
                house = grid.getRow((i, 0))
                self.hiddenSubsetHelper(house, size)
            # Iterate through Columns
            for i in range(9):
                house = grid.getColumn((0, i))
                self.hiddenSubsetHelper(house, size)
            # Iterate through Boxes
            for i in range(9):
                house = grid.getBox((int(i / 3) * 3, (i % 3) * 3))
                self.hiddenSubsetHelper(house, size)

    # Helper function for hiddenSubset
    def hiddenSubsetHelper(self, house, size):
        # pvSet is the set of values that are still possible in that house.
        pvSet = list(range(1, 10))
        for cell in house:
            if cell.value in pvSet:
                pvSet.remove(cell.value)

        combinations = itertools.combinations(pvSet, size)
        for subset in combinations:
            temp = []
            # Find the cells with any of the values in that subset
            for cell in house:
                pv = cell.possibleValues
                # Check if this cells pvs include anything in the subset
                if len([value for value in pv if value in subset]) > 0:
                    temp.append(cell)
            if len(temp) == size:
                for cell in temp:
                    cell.possibleValues = [value for value in cell.possibleValues if value in subset]

    def nakedSubset(self, grid):
        for size in range(2, 5):
            # Iterate through Rows
            for i in range(9):
                house = grid.getRow((i, 0))
                self.nakedSubsetHelper(house, size)
            # Iterate through Columns
            for i in range(9):
                house = grid.getColumn((0, i))
                self.nakedSubsetHelper(house, size)
            # Iterate through Boxes
            for i in range(9):
                house = grid.getBox((int(i / 3) * 3, (i % 3) * 3))
                self.nakedSubsetHelper(house, size)

    # Helper function for nakedSubset
    def nakedSubsetHelper(self, house, size):
        temp = []
        for cell in house:
            if cell.value == 0:
                temp.append(cell)
        combinations = itertools.combinations(temp, size)

        for subset in combinations:
            setofPVs = set()
            for cell in subset:
                setofPVs.update(set(cell.possibleValues))
            if len(setofPVs) == size:
                # Find all cells in the house not in the nakedSubset
                for otherCell in (o for o in house if o not in subset):
                    # Remove all values in the possible values of the othercell if there is overlap with the nakedSubset
                    for value in (v for v in setofPVs if v in otherCell.possibleValues):
                        otherCell.possibleValues.remove(value)

    def x_wing(self, grid):
        rows = grid.getAllRows()
        columns = grid.getAllColumns()

        row_combs = itertools.combinations(rows, 2)
        col_combs = itertools.combinations(columns, 2)

        for row_comb in row_combs:
            for col_comb in col_combs:
                self.fish_helper(row_comb, col_comb)
                self.fish_helper(col_comb, row_comb)

    # Helper function for fish
    def fish_helper(self, base_sets, cover_sets):
        # Find the cells that are the intersection between the base and cover sets
        intersections = []
        for base_set in base_sets:
            for cover_set in cover_sets:
                intersections.append(self.intersection(base_set, cover_set))

        fish_digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        for cell in intersections:
            # possible_fish_digits = self.remainingDigits(base_set)
            fish_digits = fish_digits.intersection(set(cell.possibleValues))

        for digit in fish_digits:
            # Find every cell that contains that digit in the base sets and find the intersection cells
            cells_with_digit = []
            for base_set in base_sets:
                for cell in base_set:
                    if digit in cell.possibleValues:
                        cells_with_digit.append(cell)

            # Check if the all the candidates of the digit in the base sets are contained in the cover sets
            flag = True
            for cell in cells_with_digit:
                if cell not in intersections:
                    flag = False
                    break
            if flag is True:
                # If so, we can remove all instances if that digit from the cover sets.
                for cover_set in cover_sets:
                    for cell in cover_set:
                        if cell not in intersections and digit in cell.possibleValues:
                            cell.possibleValues.remove(digit)

    # Helper function to determine if a set of cells all belong to the same row.
    def inSameRow(self, myList):
        for i in range(len(myList) - 1):
            loc1 = myList[i].location
            loc2 = myList[i + 1].location
            if loc1[0] != loc2[0]:
                return False
        return True

    # Helper function to determine if a set of cells all belong to the same column.
    def inSameCol(self, myList):
        for i in range(len(myList) - 1):
            loc1 = myList[i].location
            loc2 = myList[i + 1].location
            if loc1[1] != loc2[1]:
                return False
        return True

    # Helper function to determine if a set of cells all belong to the same box.
    def inSameBox(self, myList):
        for i in range(len(myList) - 1):
            loc1 = myList[i].location
            loc2 = myList[i + 1].location
            x1, x2 = loc1[0], loc2[0]
            y1, y2 = loc1[1], loc2[1]
            if int(x1/3) != int(x2/3) or int(y1/3) != int(y2/3):
                return False
        return True

    # Returns the first cell that is an intersection of two cross houses.
    def intersection(self, base_set, cover_set):
        for cell in (cell for cell in base_set if cell in cover_set):
            return cell

    # Returns a list of possible digits remaining in the house
    def remainingDigits(self, house):
        possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for cell in house:
            if cell.value in possibles:
                possibles.remove(cell.value)
        return possibles

"""
DuplicateError error is used if the solver accidentally ever puts a number twice in the same row, column or box.
"""
class DuplicateError(Exception):
    def __init__(self, message):
        self.message = message
