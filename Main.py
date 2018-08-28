# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 22:38:27 2018

@author: Rushan Vipani
"""

import GameReader


dirprefix = "Puzzles/"

class Cell:

    location = (0, 0)
    value = 0
    possibleValues = []
    isOriginal = False

    def __init__(self, location):
        self.value = 0
        self.location=location

    def setOriginal(self):
        self.isOriginal = True

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

class Grid:

    # grid is 10x10 grid of cells with indices of numbers from 0 to 9

    def __init__(self):
        self.grid = [[Cell((x, y)) for x in range(1, 10)]for y in range(1, 10)]

    # Takes a location as a tuple in the form of (1-9,1-9) and returns the corresponding Cell
    def getCell(self, location):
        if 1 <= location[0] <= 9 and 1 <= location[1] <= 9:
            return self.grid[location[0]-1][location[1]-1]
        else:
            print(location)
            return None

    # Takes a location as a tuple in the form of (1-9,1-9) and returns a list for the Row
    def getRow(self, location):
        pass

    # Takes a location as a tuple in the form of (1-9,1-9) and returns a list for the Column
    def getColumn(self, location):
        pass

    # Takes a location as a tuple in the form of (1-9,1-9) and returns a list for the Box
    def getBox(self, location):
        pass

    # Returns the current grid as only a 2d array of values
    def get2dArrayForm(self):
        tempgrid=[[self.getCell((x, y)) for x in range(1, 10)]for y in range(1, 10)]
        return tempgrid

    # Sets the default grid based on the given 2d array
    def setGrid(self, matrix):
        for i in range(1,10):
            for j in range(1,10):
                location = (i,j)
                cell = self.getCell(location)
                cell.setOriginal()
                cell.setValue(matrix[i-1][j-1])

    # Sets the value of a cell in a given location to the given value
    def setCell(self, location, value):
        cell = self.getCell(location)
        cell.setValue(value)

    # Establishes the initial possible values for each open cell.
    def setPossibles(self):
        pass

    # Displays the current grid state in console
    def print(self, showzero = False):
        print("_________________________")
        for i in range(1, 10):
            if not i == 1:
                print("|       |       |       |")
            print ("|", end=" ")
            for j in range(1, 10):
                value = self.getCell((i, j)).getValue()
                if value == 0 and showzero is False:
                    print(" ", end=" ")
                else:
                    print(self.getCell((i, j)).getValue(), end=" ")
                if j == 9:
                    print("|")
                elif j % 3 == 0:
                    print("|", end=" ")
            if i % 3 == 0:
                print("_________________________")


def run(problemFile):
    problemFile = dirprefix + problemFile
    g = Grid()
    g.setGrid(GameReader.getGridFromFile(problemFile))
    g.print()


if __name__ == '__main__':
    problemFile = "p1.txt"
    run(problemFile)
