# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 22:38:27 2018

@author: Rushan Vipani
"""

import GameReader
import numpy as np
import math

dirprefix = "Puzzles/"

class Cell:

    location = (0, 0)
    value = 0
    possibleValues = []
    isOriginal = False

    def __init__(self, location):
        self.value = 0
        self.location = location

    def setOriginal(self):
        self.isOriginal = True

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def setPossibleValues(self, possibles):
        self.possibleValues=possibles


class Grid:

    # grid is 10x10 grid of cells with indices of numbers from 0 to 8

    def __init__(self):
        self.grid = [[Cell((x, y)) for x in range(9)]for y in range(9)]

    # Takes a location as a tuple in the form of (0-8,0-8) and returns the corresponding Cell
    def getCell(self, location):
        if 0 <= location[0] <= 8 and 0 <= location[1] <= 8:
            return self.grid[location[0]][location[1]]
        else:
            print(location)
            return None

    # Takes a location as a tuple in the form of (0-8,0-8) and returns a list for the Row
    def getRow(self, location):
        rowOfCells = self.grid[location[0]]
        tempRow = []
        for cell in rowOfCells:
            tempRow.append(cell.getValue())
        return tempRow

    # Takes a location as a tuple in the form of (0-8,0-8) and returns a list for the Column
    def getColumn(self, location):
        grid = self.get2dArrayForm()
        betterGrid = np.array(grid)
        temp = betterGrid[:, location[1]]
        return list(temp)

    # Takes a location as a tuple in the form of (0-8,0-8) and returns a list for the Box
    def getBox(self, location):
        grid = self.get2dArrayForm()
        betterGrid = np.array(grid)
        x = math.floor(location[0] / 3) * 3
        y = math.floor(location[1] / 3) * 3
        box = betterGrid[x:x+3, y:y+3]
        return list(box.flatten())

    # Returns the current grid as only a 2d array of values
    def get2dArrayForm(self):
        tempgrid=[[self.getCell((y, x)).getValue() for x in range(9)]for y in range(9)]
        return tempgrid

    # Sets the default grid based on the given 2d array
    def setGrid(self, matrix):
        for i in range(9):
            for j in range(9):
                value = matrix[i][j]
                if not value == 0:
                    location = (i, j)
                    cell = self.getCell(location)
                    cell.setOriginal()
                    cell.setValue(value)

    # Sets the value of a cell in a given location to the given value
    def setCell(self, location, value):
        cell = self.getCell(location)
        cell.setValue(value)

    # Establishes the initial possible values for each open cell.
    def setPossibles(self):
        for i in range(9):
            for j in range(9):
                location = (i, j)
                cell = self.getCell(location)
                if not cell.isOriginal:
                    possibles=[1, 2, 3, 4, 5, 6, 7, 8, 9]
                    for v in self.getRow(location):
                        if not v==0 and v in possibles:
                            possibles.remove(v)
                    for v in self.getColumn(location):
                        if not v==0 and v in possibles:
                            possibles.remove(v)
                    for v in self.getBox(location):
                        if not v==0 and v in possibles:
                            possibles.remove(v)
                    cell.setPossibleValues(possibles)

    # Displays the current grid state in console
    def print(self, showzero = False):
        print("_________________________")
        for i in range(9):
            if not i % 3 == 0:
                print("|       |       |       |")
            print ("|", end=" ")
            for j in range(9):
                value = self.getCell((i, j)).getValue()
                if value == 0 and showzero is False:
                    print(" ", end=" ")
                else:
                    print(self.getCell((i, j)).getValue(), end=" ")
                if j == 8:
                    print("|")
                elif j % 3 == 2:
                    print("|", end=" ")
            if i % 3 == 2:
                print("_________________________")


def run(problemFile):
    problemFile = dirprefix + problemFile
    g = Grid()
    g.setGrid(GameReader.getGridFromFile(problemFile))
    g.setPossibles()
    g.print()


if __name__ == '__main__':
    problemFile = "p1.txt"
    run(problemFile)
