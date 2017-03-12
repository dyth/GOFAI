#!/usr/bin/env python
"""script to generate `sudoku.py` for a 3 * 3 grid"""

def board():
    'return string of all board variables'
    board = []
    for i in range(81):
        board.append(i)
    return board


def rows():
    'return list of list of tile indexes representing all rows'
    rows = []
    for i in range(9):
        nestedRow = []
        for j in range(9):
            nestedRow.append(9*i + j)
        rows.append(nestedRow)
    return rows


def columns():
    'return list of list of tile indexes representing all columns'
    columns = []
    for i in range(9):
        nestedColumn = []
        for j in range(9):
            nestedColumn.append(9*j + i)
        columns.append(nestedColumn)
    return columns


def boxes():
    'return list of list of tile indexes representing all boxes'
    boxes = []
    for x in range(3):
        for y in range(3):
            nestedBox = []
            for i in range(3):
                for j in range(3):
                    nestedBox.append(27*y + 9*i + 3*x + j)
            boxes.append(nestedBox)
    return boxes


def toStatement(board):
    'convert a board list into a string for Prolog'
    prolog = ''
    for b in board:
        prolog += 'H' + str(b) + ", "
    return prolog[:-2]


def toConstraints(board, constraints):
    'convert a declaration and its constraints into a prolog relation'
    relation = ''
    relation += '([' + board + ']) :- '
    for c in constraints:
        relation += 'diff([' + str(c) + ']), '
    return relation[:-2]
    

# create a board and its constraints
board = board()
rows = rows()
columns = columns()
boxes = boxes()

# convert lists into prolog strings
board = toStatement(board)
rows = [toStatement(r) for r in rows]
columns = [toStatement(c) for c in columns]
boxes = [toStatement(b) for b in boxes]

# output prolog relations
rows = toConstraints(board, rows)
columns = toConstraints(board, columns)
boxes = toConstraints(board, boxes)

# formatting for relations
rows = 'rows' + rows + '.\n\n'
columns = 'columns' + columns + '.\n\n'
boxes = 'boxes' + boxes + '.\n\n'

# create a file called sudoku.pl with all of the constraints 
sudokuFile = open("sudoku.pl", "w") 
sudokuFile.write(":- use_module(library(bounds)).\n\n")
sudokuFile.write("diff(L) :- L in 1..9, all_different(L).\n\n")
sudokuFile.write(rows)
sudokuFile.write(columns)
sudokuFile.write(boxes)
sudokuFile.write("sudoku(L) :- rows(L), columns(L), boxes(L), label(L).")
sudokuFile.close()

print "The program can be queried using the following command, with some of the tile coordinates changed:"
print "sudoku([" + board + "])."
