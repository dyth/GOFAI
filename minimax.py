#!/usr/bin/env python
"""the minimax procedure with alpha beta pruning"""
from noughtsCrosses import *


class node:
    'a node in a list tree'

    def __init__(self, board, moves, player):
        'initialise new node with a board'
        self.board = board
        self.player = player
        self.winner = evaluate(board)
        if not self.winner:
            self.next = nextPlayer(self.player)
            self.moves = [node(move, moveAll(move, self.next), self.next)
                              if (move != None) else None
                          for move in moves]


        
me = node(initialBoard, moveAll(1, initialBoard), 1)
print me

print moveAll(1, initialBoard)
