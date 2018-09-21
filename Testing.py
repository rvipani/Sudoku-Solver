# Testing.py
"""
Testing holds the unittest used to test the key functionality of the project.
All unittests are held in the MyTest class
"""
import unittest
import Main
import GameReader
import Solver


class BasicTests(unittest.TestCase):
    # 6 Test cases
    def test_gridSetup(self):
        g = Main.Grid()
        self.assertEqual(0, g.getCell((0, 0)).getValue())

    def test_importing(self):
        problemFile = "Puzzles/Testing/test1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        self.assertEqual(7, g.getCell((0, 0)).getValue())

    def test_getRow(self):
        problemFile = "Puzzles/Testing/test1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        correctRow=[7, 6, 8, 5, 0, 2, 1, 4, 9]
        self.assertEqual(correctRow, g.cellsToVals(g.getRow((0, 0))))
        self.assertEqual(correctRow, g.cellsToVals(g.getRow((0, 4))))

    def test_getColumn(self):
        problemFile = "Puzzles/Testing/test1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        correctColumn = [7, 3, 4, 6, 0, 1, 5, 8, 9]
        self.assertEqual(correctColumn, g.cellsToVals(g.getColumn((0, 0))))
        self.assertEqual(correctColumn, g.cellsToVals(g.getColumn((5, 0))))

    def test_getBox(self):
        problemFile = "Puzzles/Testing/test1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        correctBox = [7, 6, 8, 3, 0, 0, 4, 0, 0]
        self.assertEqual(correctBox, g.cellsToVals(g.getBox((0, 0))))
        self.assertEqual(correctBox, g.cellsToVals(g.getBox((2, 2))))

    def test_setPossibles(self):
        problemFile = "Puzzles/Testing/test1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        g.setPossibles()
        correctPossibles = [5, 9]
        cell = g.getCell((1, 1))
        self.assertEqual(correctPossibles, cell.possibleValues)


class SolvingTests(unittest.TestCase):
    # 3 Test cases
    def test_isUnsolved(self):
        problemFile = "Puzzles/Testing/test1.txt"
        g = Main.Grid()
        g.setGrid(GameReader.getGridFromFile(problemFile))
        s = Solver.Solver()

        # Check for row duplicates
        g.setCell((1, 3), 7)
        with self.assertRaises(Solver.DuplicateError) as cm:
            s.isUnsolved(g)
        exception = cm.exception
        message = exception.message
        self.assertEqual("Row 1 contains a duplicate", message)
        g.setCell((1, 3), 0)

        # Check for column duplicates
        g.setCell((4, 0), 7)
        with self.assertRaises(Solver.DuplicateError) as cm:
            s.isUnsolved(g)
        exception = cm.exception
        message = exception.message
        self.assertEqual("Column 0 contains a duplicate", message)
        g.setCell((4, 0), 0)

        # Check for box duplicates
        g.setCell((1, 1), 8)
        with self.assertRaises(Solver.DuplicateError) as cm:
            s.isUnsolved(g)
        exception = cm.exception
        message = exception.message
        self.assertEqual("Box 0 contains a duplicate", message)
        g.setCell((1, 1), 0)

        # Check that check for 0s works properly
        self.assertTrue(s.isUnsolved(g))

    def test_nakedSingle(self):
        problemFile = "Puzzles/Testing/test1.txt"
        g = Main.Grid()
        g.setup(problemFile)
        s = Solver.Solver()
        s.nakedSingle(g)
        cell = g.getCell((0, 4))
        self.assertEqual(3, cell.getValue())

    def test_hiddenSingles(self):
        problemFile = "Puzzles/Testing/test2.txt"
        g = Main.Grid()
        g.setup(problemFile)
        s = Solver.Solver()
        s.hiddenSingle(g)
        cell = g.getCell((2, 3))
        self.assertEqual(6, cell.getValue())

    def test_pointing(self):
        problemFile = "Puzzles/Testing/test3.txt"
        g = Main.Grid()
        g.setup(problemFile)
        s = Solver.Solver()
        # Before
        self.assertEqual([3, 5], g.getCell((2, 6)).possibleValues)
        s.pointing(g)
        # After
        self.assertEqual([3], g.getCell((2, 6)).possibleValues)

        problemFile = "Puzzles/Testing/test4.txt"
        g = Main.Grid()
        g.setup(problemFile)
        # Before
        for cell in g.getRow((6, 0)):
            if cell.location[1] != 4:
                self.assertTrue(1 in cell.possibleValues)
        s.pointing(g)
        # After
        for cell in g.getRow((6, 0)):
            if cell.location[1] != 3 and cell.location[1] != 5:
                self.assertTrue(1 not in cell.possibleValues)


    def test_claiming(self):
        problemFile = "Puzzles/Testing/test5.txt"
        g = Main.Grid()
        g.setup(problemFile)
        s = Solver.Solver()
        # Before
        self.assertEqual([4, 7], g.getCell((2, 1)).possibleValues)
        s.claiming(g)
        # After
        self.assertEqual([4], g.getCell((2, 1)).possibleValues)

        problemFile = "Puzzles/Testing/test6.txt"
        g = Main.Grid()
        g.setup(problemFile)
        # Before
        for cell in g.getBox((0, 3)):
            if cell.location[1] != 5:
                self.assertTrue(4 in cell.possibleValues)
        s.claiming(g)
        # After
        for cell in g.getBox((0, 3)):
            if cell.location[1] != 5:
                self.assertTrue(4 not in cell.possibleValues)

    def test_hiddenSubset(self):
        problemFile = "Puzzles/Testing/test7.txt"
        g = Main.Grid()
        g.setup(problemFile)
        s = Solver.Solver()
        # Before
        self.assertEqual([1, 6, 9], g.getCell((4, 8)).possibleValues)
        s.hiddenSubsetHelper(g.getColumn((0, 8)), 2)
        # After
        self.assertEqual([1, 9], g.getCell((4, 8)).possibleValues)

        problemFile = "Puzzles/Testing/test8.txt"
        g = Main.Grid()
        g.setup(problemFile)
        s = Solver.Solver()
        # Before
        self.assertEqual([1, 2, 4, 5], g.getCell((8, 1)).possibleValues)
        self.assertEqual([2, 5, 6], g.getCell((8, 2)).possibleValues)
        s.hiddenSubset(g)
        # After
        self.assertEqual([2, 4, 5], g.getCell((8, 1)).possibleValues)
        self.assertEqual([2, 5], g.getCell((8, 2)).possibleValues)

        problemFile = "Puzzles/Testing/test9.txt"
        g = Main.Grid()
        g.setup(problemFile)
        s = Solver.Solver()
        # Before
        self.assertEqual([3, 4, 5, 6, 8], g.getCell((6, 4)).possibleValues)
        self.assertEqual([2, 4, 5, 6], g.getCell((7, 4)).possibleValues)
        s.hiddenSubset(g)
        # After
        self.assertEqual([4, 5, 8], g.getCell((6, 4)).possibleValues)
        self.assertEqual([2, 4, 5], g.getCell((7, 4)).possibleValues)


if __name__ == '__main__':
    unittest.main()
