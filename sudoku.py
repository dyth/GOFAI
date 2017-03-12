#!/usr/bin/env python
"""script to generate `sudoku.py` for a 3 * 3 grid"""

def board():
    'return string of all board variables'
    board = []
    for i in range(81):
        board.append(i)
    return board


def rows(board):
    'return list of list of tile indexes representing all rows'
    rows = []
    for i in range(9):
        nestedRow = []
        for j in range(9):
            nestedRow.append(board[9*i + j])
        rows.append(nestedRow)
    return rows


def columns(board):
    'return list of list of tile indexes representing all columns'
    columns = []
    for i in range(9):
        nestedColumn = []
        for j in range(9):
            nestedColumn.append(board[9*j + i])
        columns.append(nestedColumn)
    return columns


def boxes(board):
    'return list of list of tile indexes representing all boxes'
    boxes = []
    for x in range(3):
        for y in range(3):
            nestedBox = []
            for i in range(3):
                for j in range(3):
                    nestedBox.append(board[27*y + 9*i + 3*x + j])
            boxes.append(nestedBox)
    return boxes


board = board()
rows = rows(board)
columns = columns(board)
boxes = boxes(board)

print board
print rows
print columns
print boxes
