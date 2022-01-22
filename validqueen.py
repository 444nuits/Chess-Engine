"""
Get Valid Queen Moves
"""

import chessengine
import validbishop
import validrook

def ValidWhiteQueen(gs, row, col):
    ValidQueenMoves = []
    ValidQueenMoves+=validbishop.ValidWhiteBishop(gs, row, col)
    ValidQueenMoves+=validrook.ValidWhiteRook(gs, row, col)
    return ValidQueenMoves

def ValidBlackQueen(gs, row, col):
    ValidQueenMoves = []
    ValidQueenMoves+=validbishop.ValidBlackBishop(gs, row, col)
    ValidQueenMoves+=validrook.ValidBlackRook(gs, row, col)
    return ValidQueenMoves

