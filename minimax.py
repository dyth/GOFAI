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
        self.moves = None
        # if a winner does not exist, swap the players and do all possible moves
        if (self.winner == None) and (None in self.board):
            self.next = nextPlayer(self.player)
            self.moves = [node(self.next, move) if (move != None) else None
                          for move in moveAll(self.next, self.board)]
            
            
def minimax(n, i, player):
    'recursively interleave taking the maximum and then minimum values of lists and sublists'
    # if there is no winner, do recursion downwards
    if (n != None):
        if (n.moves != None):
            moves = [minimax(m, (i+1)%2, nextPlayer(player)) for m in n.moves]
            # Take the maximum or minimum depending on whether origin distance
            if (i == 1):
                move = max(moves)
            elif (i == 0):
                move = min(moves)
        # At nodes, if the player is the winner, then assign positive score.
        # Otherwise, assign negative score
        elif (player == n.winner):
            move = 1
        elif (nextPlayer(player) == n.winner):
            move = -1
        elif (None == n.winner and n.moves == None):
            move = 0
        return move


def decision(player, board):
    'input player ID and current state of board to generate the next state'
    root = node(player, board)
    moves = [minimax(n, 0, nextPlayer(player)) for n in root.moves]
    position = moves.index(max(moves))
    return move(player, board, position / 3, position % 3)
