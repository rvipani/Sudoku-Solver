# Sudoku-Solver

### A Solver for Sudoku puzzles.
### Author Rushan Vipani
### Project Created 8/15/2018
### Last Update 9/21/2018

### Steps

1. Create Basic Structure of Project
2. Add ability to import Sudoku puzzles as txt files.  
    The solver can take a file as input to solve. The file must contain only the values for each cell with each empty cell represented as a 0. Each value must also be space delimited.  
    Ex:   
    7 6 8 5 0 2 1 4 9  
    3 0 0 0 7 0 8 2 6  
    4 0 0 1 8 0 0 0 7  
    6 0 4 0 1 7 0 5 2  
    0 3 5 4 6 0 0 0 8  
    1 0 0 2 0 0 0 9 0  
    5 1 0 0 0 0 4 0 3  
    8 4 0 7 0 5 0 0 1  
    9 7 6 3 4 0 2 8 0  
    Comments can also be added with "#" and "//". Any line with those indicators will be ignored when reading the file. 
3. Add ability to find possible values for each cell. 
4. Add ability to solve Soduku puzzle and display result
    Include support for following solving strategies:   
    a. Hidden Singles  
    b. Naked Singles  
    c. Locked Candidates (Pointing and Claiming)  
    d. Hidden Subsets
5. Create UI for importing Soduku puzzle and finished output
6. Add image recognition support for easier importing. ????
