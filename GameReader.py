def getGridFromFile(fileName):
    file = open(fileName, "r")
    grid = []
    for line in file:
        #print(line)
        split = line.split(" ")
        temp = []
        for value in split:
            #print(value)
            temp.append(int(value))
        grid.append(temp)
    print(grid)
    return grid
