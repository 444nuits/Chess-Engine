"""
Get Valid Bishop Moves
"""

import chessengine

def ValidWhiteBishop(gs, row, col):
    saverow =  row
    savecol = col
    ValidBishopMoves = []
    while(col-1>=0 and row-1>=0):
        if (gs.board[row-1][col-1] == "--"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col-1, row-1)))
        if (gs.board[row-1][col-1][0] == "b"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col-1, row-1)))
            break
        if (gs.board[row-1][col-1][0] == "w"):
            break
        col-=1
        row-=1
    col = savecol
    row = saverow
    while(col-1>=0 and row+1<8):
        if (gs.board[row+1][col-1] == "--"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col-1, row+1)))
        if (gs.board[row+1][col-1][0] == "b"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col-1, row+1)))
            break
        if (gs.board[row+1][col-1][0] == "w"):
            break
        col-=1
        row+=1
    col = savecol
    row = saverow
    while (col +1<8 and row-1 >= 0):
        if (gs.board[row - 1][col + 1] == "--"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col + 1, row - 1)))
        if (gs.board[row - 1][col + 1][0] == "b"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col + 1, row - 1)))
            break
        if (gs.board[row - 1][col + 1][0] == "w"):
            break
        col += 1
        row -= 1
    col = savecol
    row = saverow
    while (col+1<8 and row +1< 8):
        if (gs.board[row + 1][col + 1] == "--"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col + 1, row + 1)))
        if (gs.board[row + 1][col + 1][0] == "b"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col + 1, row + 1)))
            break
        if (gs.board[row + 1][col + 1][0] == "w"):
            break
        col += 1
        row += 1
    col = savecol
    row = saverow
    return ValidBishopMoves


def ValidBlackBishop(gs, row, col):
    saverow = row
    savecol = col
    ValidBishopMoves = []
    while (col-1 >= 0 and row-1 >= 0):
        if (gs.board[row - 1][col - 1] == "--"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col - 1, row - 1)))
        if (gs.board[row - 1][col - 1][0] == "w"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col - 1, row - 1)))
            break
        if (gs.board[row - 1][col - 1][0] == "b"):
            break
        col -= 1
        row -= 1
    col = savecol
    row = saverow
    while (col-1 >= 0 and row+1 < 8):
        if (gs.board[row + 1][col - 1] == "--"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col - 1, row + 1)))
        if (gs.board[row + 1][col - 1][0] == "w"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col - 1, row + 1)))
            break
        if (gs.board[row + 1][col - 1][0] == "b"):
            break
        col -= 1
        row += 1
    col = savecol
    row = saverow
    while (col+1 < 8 and row-1 >= 0):
        if (gs.board[row - 1][col + 1] == "--"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col + 1, row - 1)))
        if (gs.board[row - 1][col + 1][0] == "w"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col + 1, row - 1)))
            break
        if (gs.board[row - 1][col + 1][0] == "b"):
            break
        col += 1
        row -= 1
    col = savecol
    row = saverow
    while (col+1 < 8 and row+1 < 8):
        if (gs.board[row + 1][col + 1] == "--"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col + 1, row + 1)))
        if (gs.board[row + 1][col + 1][0] == "w"):
            ValidBishopMoves.append(chessengine.Move(gs.board, o=(savecol, saverow), t=(col + 1, row + 1)))
            break
        if (gs.board[row + 1][col + 1][0] == "b"):
            break
        col += 1
        row += 1
    col = savecol
    row = saverow
    return ValidBishopMoves