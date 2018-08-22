# Pulls from a file and turns the file into a grid. Grid format is 9x9 space delimited.
def getGridFromFile(fileName):
    file = open(fileName, "r")
    grid = []
    for line in file:
        split = line.split(" ")
        temp = []
        for value in split:
            temp.append(int(value))
        grid.append(temp)
    #print(grid)
    return grid
