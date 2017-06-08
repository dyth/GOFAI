#!/usr/bin/env python
"""Noughts and crosses in Python"""
import numpy as np

board = [['', '', ''], ['', '', ''], ['', '', '']]

class node:
    'node within a tree where moves can be made'

    def __init__(self, board):
        'initialise new node with a board'
        self.board = board
