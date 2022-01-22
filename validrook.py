"""
Get Valid Rook Moves
"""

import chessengine
import chessmain

def ValidWhiteRook(gs, row, col):
    ValidRookMoves = []
    board = gs.board
    for i in range(col-1, -1, -1):
        if(board[row][i] == "--"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(i, row)))
        if (board[row][i][0] == "b"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(i, row)))
            break
        if (board[row][i][0] == "w"):
            break
    for i in range(row-1, -1, -1):
        if(board[i][col] == "--"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(col, i)))
        if (board[i][col][0] == "b"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(col, i)))
            break
        if (board[i][col][0] == "w"):
            break
    for i in range(col+1, chessmain.DIMENSION):
        if(board[row][i] == "--"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(i, row)))
        if (board[row][i][0] == "b"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(i, row)))
            break
        if (board[row][i][0] == "w"):
            break
    for i in range(row+1, chessmain.DIMENSION):
        if(board[i][col] == "--"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(col, i)))
        if (board[i][col][0] == "b"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(col, i)))
            break
        if (board[i][col][0] == "w"):
            break
    return ValidRookMoves

def ValidBlackRook(gs, row, col):
    ValidRookMoves = []
    board = gs.board
    for i in range(col - 1, -1, -1):
        if (board[row][i] == "--"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(i, row)))
        if (board[row][i][0] == "w"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(i, row)))
            break
        if (board[row][i][0] == "b"):
            break
    for i in range(row - 1, -1, -1):
        if (board[i][col] == "--"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(col, i)))
        if (board[i][col][0] == "w"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(col, i)))
            break
        if (board[i][col][0] == "b"):
            break
    for i in range(col + 1, chessmain.DIMENSION):
        if (board[row][i] == "--"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(i, row)))
        if (board[row][i][0] == "w"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(i, row)))
            break
        if (board[row][i][0] == "b"):
            break
    for i in range(row + 1, chessmain.DIMENSION):
        if (board[i][col] == "--"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(col, i)))
        if (board[i][col][0] == "w"):
            ValidRookMoves.append(chessengine.Move(board, o=(col, row), t=(col, i)))
            break
        if (board[i][col][0] == "b"):
            break
    return ValidRookMoves