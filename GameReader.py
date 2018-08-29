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
            temp.append(int(value))
        grid.append(temp)
    # print(grid)
    file.close()
    return grid
