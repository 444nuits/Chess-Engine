"""
Get Valid Pawn Moves
"""

import chessengine

def ValidWhitePawn(gs, row, column):
    board = gs.board
    ValidPawnMoves = []
    if (row>0):
        if (column > 0):
            if(board[row - 1][column - 1][0] == "b"):
                ValidPawnMoves.append(chessengine.Move(board, o=(column, row), t=(column-1, row-1)))
        if (column < 7):
            if (board[row - 1][column + 1][0] == "b"):
                ValidPawnMoves.append(chessengine.Move(board, o=(column, row), t=(column + 1, row - 1)))
        if (board[row - 1][column] == "--"):
            ValidPawnMoves.append(chessengine.Move(board, o=(column, row), t=(column, row - 1)))
        if(row == 6):
            if (board[row - 1][column] == "--"):
                if (board[row - 2][column] == "--"):
                    ValidPawnMoves.append(chessengine.Move(board, o=(column, row), t=(column, row - 2)))
    enpassant = getEnPassant(gs.movelog)
    if(enpassant != [-1, -1]):
        if(((enpassant[0] == column+1) or (enpassant[0] == column-1)) and (enpassant[1] == row)):
            ValidPawnMoves.append(chessengine.Move(board, o=(column, row), t=(enpassant[0], row-1), enpassant=True))
    return ValidPawnMoves


def ValidBlackPawn(gs, row, column):
    board = gs.board
    ValidPawnMoves = []
    if (row < 7):
        if(column > 0):
            if(board[row + 1][column - 1][0] == "w"):
                ValidPawnMoves.append(chessengine.Move(board, o=(column, row), t=(column - 1, row + 1)))
        if(column < 7):
            if (board[row + 1][column + 1][0] == "w"):
                ValidPawnMoves.append(chessengine.Move(board, o=(column, row), t=(column + 1, row + 1)))
        if (board[row + 1][column] == "--"):
            ValidPawnMoves.append(chessengine.Move(board, o=(column, row), t=(column, row + 1)))
        if(row == 1):
            if (board[row + 1][column] == "--"):
                if (board[row + 2][column] == "--"):
                    ValidPawnMoves.append(chessengine.Move(board, o=(column, row), t=(column, row + 2)))
    enpassant = getEnPassant(gs.movelog)
    if (enpassant != [-1, -1]):
        if (((enpassant[0] == column + 1) or (enpassant[0] == column - 1)) and (enpassant[1] == row)):
            ValidPawnMoves.append(chessengine.Move(board, o=(column, row), t=(enpassant[0], row + 1), enpassant=True))
    return ValidPawnMoves

def getEnPassant(movelog):
    if(movelog != []):
        move = movelog[-1]
        if(move.piecemoved[1] == "p"):
            if((move.to[1] - move.origin[1]) == 2 or (move.to[1] - move.origin[1]) == -2):
                return [move.to[0], move.to[1]]
    return [-1, -1]