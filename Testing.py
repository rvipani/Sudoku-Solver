import unittest
import Main
import GameReader


class MyTest(unittest.TestCase):
    def testGridSetup(self):
        g = Main.Grid()
        self.assertEqual(0, g.getCell((1, 1)).getValue())

    def testimporting(self):
        problemFile = "Puzzles/p1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        self.assertEqual(7, g.getCell((1, 1)).getValue())

    def testPossibles(self):
        problemFile = "Puzzles/p1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        g.setPossibles()
        correctPossibles = [1, 2, 3]
        cell = g.getCell((1, 1))
        self.assertEqual(correctPossibles, cell.possibleValues)


if __name__ == '__main__':
    unittest.main()
