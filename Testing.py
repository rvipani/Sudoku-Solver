# Testing.py
"""
Testing holds the unittest used to test the key functionality of the project.
All unittests are held in the MyTest class
"""
import unittest
import Main
import GameReader
from Solver import Solver


class BasicTests(unittest.TestCase):
    def test_gridSetup(self):
        g = Main.Grid()
        self.assertEqual(0, g.getCell((0, 0)).getValue())

    def test_importing(self):
        problemFile = "Puzzles/p1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        self.assertEqual(7, g.getCell((0, 0)).getValue())

    def test_getRow(self):
        problemFile = "Puzzles/p1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        correctRow=[7, 6, 8, 5, 0, 2, 1, 4, 9]
        self.assertEqual(correctRow, g.cellsToVals(g.getRow((0, 0))))
        self.assertEqual(correctRow, g.cellsToVals(g.getRow((0, 4))))

    def test_getColumn(self):
        problemFile = "Puzzles/p1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        correctColumn = [7, 3, 4, 6, 0, 1, 5, 8, 9]
        self.assertEqual(correctColumn, g.cellsToVals(g.getColumn((0, 0))))
        self.assertEqual(correctColumn, g.cellsToVals(g.getColumn((5, 0))))

    def test_getBox(self):
        problemFile = "Puzzles/p1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        correctBox = [7, 6, 8, 3, 0, 0, 4, 0, 0]
        self.assertEqual(correctBox, g.cellsToVals(g.getBox((0, 0))))
        self.assertEqual(correctBox, g.cellsToVals(g.getBox((2, 2))))

    def test_setPossibles(self):
        problemFile = "Puzzles/p1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        g.setPossibles()
        correctPossibles = [5, 9]
        cell = g.getCell((1, 1))
        self.assertEqual(correctPossibles, cell.possibleValues)


class SolvingTests(unittest.TestCase):

    def test_duplicateError(self):
        problemFile = "Puzzles/p1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        g.setCell((1, 3), 7)
        g.print()
        pass

    def test_nakedSingle(self):
        problemFile = "Puzzles/p1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        g.setPossibles()
        s = Solver()
        s.nakedSingle(g)
        cell = g.getCell((0, 4))
        self.assertEqual(3, cell.getValue())

    def test_hiddenSingles(self):
        pass

if __name__ == '__main__':
    unittest.main()
