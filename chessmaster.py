#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Chess Game """


import time


class ChessPiece(object):
    """Class defining chess piece"""

    prefix = ''
    
    def __init__(self, position):
        """Constructor

        Args:
            position(string): chess position initially.

        Attributes:
            Prefix(string): chess piece's prefix
            position: instance position
        """

        self.position = position
        self.moves = []
        if not self.is_legal_move(position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        """finds a algebraic location in tuples for given chess piece.

        Args:
            tile(string): string format of location for chess piece.

        Return:
            Mixed: Returns a tuple or None.
        """
        
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
        """testing whether given chess piece location is on the chess board.

        Args:
            position(string): position to be tested.

        Returns:
            Boolean: True if position is legal otherwise False.
        """
        if self.algebraic_to_numeric(position) is not None:
            return True
        else:
            return False           
            
    def move(self, position):
        """Moving chess piece.

        Args:
            position(string): Algebraic expression.

        Returns:
            a tuple.
        """
        
        if self.is_legal_move(position) and position != self.position:
            oldposition = prefix + self.position
            newposition = prefix + position
            timestamp = time.time()
            l_tup = (oldposition, newposition, timestamp)
            self.moves.append(l_tup)
            self.position = position
            return l_tup
        else:
            return False


class Rook(ChessPiece):
    """ Rook Chess piece"""

    prefix = 'R'

    def is_legal_move(self, position):
        """Finds out whether Rook move is legal.

        Args:
            position(string): position to be tested.

        Returns:
            Boolean: True if move is legal, if not False.
        """
        
        cur_pos = self.algebraic_to_numeric(self.position)
        new_pos = self.algebraic_to_numeric(position)
        compare1 = cur_pos[0] == new_pos[0] and cur_pos[1] != new_pos[1]
        compare2 = cur_pos[0] != new_pos[0] and cur_pos[1] == new_pos[1]
        timestamp = time.time()
        if compare1 or compare2:
            return (prefix + cur_pos, prefix + new_pos, timestamp)
        else:
            return False

class Bishop(ChessPiece):
    """Bishop Chess piece"""
    
    prefix = 'B'
    
    def is_legal_move(self, position):
        """Finds out whether Bishop move is legal.

        Args:
            position(string): position to be tested.

        Returns:
            Boolean: True if move is legal, if not False.
        """
        
        cur_pos = self.algebraic_to_numeric(self.position)
        new_pos = self.algebraic_to_numeric(position)
        pos_1 = (cur_pos[0] - new_pos[0]) == (cur_pos[1] - new_pos[1])
        pos_2 = (cur_pos[0] + new_pos[0]) == (cur_pos[1] + new_pos[1])
        timestamp = time.time()
        if pos_1 or pos_2:
            return (prefix + cur_pos, prefix + new_pos, timestamp)
        else:
            return False

class King(ChessPiece):
    """King chess piece"""
    
    prefix = 'K'

    def is_legal_move(self, position):
        """Finds out whether Bishop move is legal.

        Args:
            position(string): position to be tested.

        Returns:
            Boolean: True if move is legal, if not False.
        """
        
        cur_pos = self.algebraic_to_numeric(self.position)
        new_pos = self.algebraic_to_numeric(position)
        move_1 = cur_pos[0] + 1 and cur_pos[1] + 1
        move_2 = cur_pos[0] + 1 or cur_pos[1] + 1
        timestamp = time.time()
        if not move_1 and move_2:
            return False
        else:
            return (prefix + cur_pos, prefix + new_pos, timestamp)

class ChessMatch(ChessPiece):
    """Chess match class"""
    def __init__(self, pieces=None):
        self.log = []
        if pieces is not None:
            self.pieces = pieces
        else:
            self.reset()
    def reset(self):
        self.pieces = {'Ra1': Rook('a1'),
                       'Rh1': Rook('h1'),
                       'Ra8': Rook('a8'),
                       'Rh8': Rook('h8'),
                       'Bc1': Bishop('c1'),
                       'Bf1': Bishop('f1'),
                       'Bc8': Bishop('c8'),
                       'Bf8': Bishop('f8'),
                       'Ke1': King('e1'),
                       'Ke8': King('e8')}
        self.log = []
        return None

    def move(self, piece, position):


    def __len__(self):
        return len(self.log)
