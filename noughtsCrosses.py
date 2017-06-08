#!/usr/bin/env python
"""noughts and crosses in Python"""
import numpy as np
import copy

initial_board = [None, None, None, None, None, None, None, None, None]
players = [0, 1]

def move(player, board, pos1, pos2):
    'board[pos1][pos2] = player'
    moved = copy.deepcopy(board)
    index = 3 * pos1 + pos2
    if (moved[index] == None):
        moved[index] = player
        return moved
    else:
        return None


def win(board):
    'determine if there is a winner in the board'
    winner = [7, 56, 73, 84, 146, 273, 292, 448]
    for player in players:
        state = 0
        for i in range(9):
            state += (int(board[i] == player) << i)
        if not set([state & w for w in winner]).isdisjoint(winner):
            return player



class node:
    'node within a tree where moves can be made'

    def __init__(self, board, moves):
        'initialise new node with a board'
        self.board = board
        self.moves = moves
