#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Chess Game """


import time


class ChessPiece(object):
    prefix = ''
    
    def __init__(self, position):
        if self.is_legal_move(position) is False:
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        else:
            self.position = position
            self.moves = []

    def algebraic_to_numeric(self, tile=''):
        self.tile = tile
        letters = 'abcdefgh'
        numbers = range(1, 9)
        if (tile[0] in letters) and (int(tile[1]) in numbers):
            l_position = letters.find(tile[0])
            num_position = int(tile[1])-1
            return (l_position, num_position)
        else:
            return None
                
    def is_legal_move(self, position):
        if self.algebraic_to_numeric(position) is not None:
            return True
        else:
            return False           
            
    def move(self, position):
        if self.is_legal_move(position) is not None:
            oldposition = self.position
            newposition = position
            timestamp = time.time()
            l_tup = (oldposition, newposition, timestamp)
            self.moves.append(l_tup)
            return l_tup
        else:
            False


class Rook(ChessPiece):
    prefix = 'R'
    def is_legal_move(self, position):
        if self.algebraic_to_numeric(position) is not None:
            cur_pos = self.position
            new_pos = position
        else:
            return False    
    
