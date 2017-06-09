#!/usr/bin/env python
"""the minimax procedure with alpha beta pruning"""
from noughtsCrosses import *


class node:
    'a node in a list tree'

    def __init__(self, player, board):
        'initialise new node with a board'
        # set conditions
        self.board = board
        self.player = player
        self.winner = evaluate(board)
        # if a winner does not exist, swap the players and do all possible moves
        if self.winner == None:
            self.next = nextPlayer(self.player)
            self.moves = [node(self.next, move) if (move != None) else None
                          for move in moveAll(self.next, self.board)]

            
def largestIndex(l):
    'return the index of the largest item in l'
    return l.index(max(l))


def smallestIndex(l):
    'return the index of the smallest item in l'
    return l.index(min(l))



me = node(1, initialBoard)
print x, o, draws
