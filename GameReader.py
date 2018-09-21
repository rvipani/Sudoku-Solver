# GameReader.py
"""
# Pulls from a file and turns the file into a grid. Grid format is 9x9 space delimited.
# Lines with "#" or "//" are ignored when reading.
"""


def getGridFromFile(fileName):
    file = open(fileName, "r")
    grid = []
    for line in file:
        if "#" in line or "//" in line:
            continue
        split = line.split(" ")
        temp = []
        for value in split:
            v = int(value)
            if v > 9:
                message = "All values must be between 0 and 9 inclusively"
                raise InputError(message)
            temp.append(int(value))
        if len(temp) != 9:
            message = "The inputted problem does not contain 9 columns"
            raise InputError(message)
        grid.append(temp)
    file.close()
    if len(grid) != 9:
        message = "The inputted problem does not contain 9 rows"
        raise InputError(message)
    return grid


"""
InputGrid Error is used if the file inputted to the grid is not a 9x9 since that is the only grid size supported. 
"""
class InputError(Exception):
    def __init__(self, message):
        self.message = message
