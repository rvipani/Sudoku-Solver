import unittest
import Main
import GameReader


class MyTest(unittest.TestCase):
    def testGridSetup(self):
        g = Main.Grid()
        self.assertEqual(0, g.getCell((0, 0)).getValue())

    def testimporting(self):
        problemFile = "Puzzles/p1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        self.assertEqual(7, g.getCell((0, 0)).getValue())

    def testgetRow(self):
        problemFile = "Puzzles/p1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        correctRow=[7, 6, 8, 5, 0, 2, 1, 4, 9]
        self.assertEqual(correctRow, g.getRow((0, 0)))

    def testgetColumn(self):
        problemFile = "Puzzles/p1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        correctColumn = [7, 3, 4, 6, 0, 1, 5, 8, 9]
        self.assertEqual(correctColumn, g.getColumn((0, 0)))
        self.assertEqual(correctColumn, g.getColumn((5, 0)))

    def testgetBox(self):
        problemFile = "Puzzles/p1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        correctBox = [7, 6, 8, 3, 0, 0, 4, 0, 0]
        self.assertEqual(correctBox, g.getBox((0, 0)))
        self.assertEqual(correctBox, g.getBox((2, 2)))

    def testPossibles(self):
        problemFile = "Puzzles/p1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        g.setPossibles()
        correctPossibles = [5, 9]
        cell = g.getCell((1, 1))
        self.assertEqual(correctPossibles, cell.possibleValues)


if __name__ == '__main__':
    unittest.main()
