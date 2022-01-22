"""
Get Valid King Moves
"""

import chessengine
import chessmain
import valid


def ValidWhiteKing(gs, row, col):
    ValidKingMoves = []
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(0, 8):
        if ((0 <= col + dx[i]) and (col + dx[i] < 8) and (0 <= row + dy[i]) and (row + dy[i] < 8)):
            if ((gs.board[row + dy[i]][col + dx[i]][0] == "-") or (gs.board[row + dy[i]][col + dx[i]][0] == "b")):
                ValidKingMoves.append(chessengine.Move(gs.board, o=(col, row), t=(col + dx[i], row + dy[i])))
    Castle = getWhiteCastle(gs)
    if(Castle == True):
        ValidKingMoves.append(chessengine.Move(gs.board, o=(col, row), t=(6, 7), castle=True))
    bigCastle = getbigWhiteCastle(gs)
    if(bigCastle):
        ValidKingMoves.append(chessengine.Move(gs.board, o=(col, row), t=(2, 7), bigcastle=True))
    return ValidKingMoves

def ValidBlackKing(gs, row, col):
    ValidKingMoves = []
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(0, 8):
        if ((0 <= col + dx[i]) and (col + dx[i] < 8) and (0 <= row + dy[i]) and (row + dy[i] < 8)):
            if ((gs.board[row + dy[i]][col + dx[i]][0] == "-") or (gs.board[row + dy[i]][col + dx[i]][0] == "w")):
                ValidKingMoves.append(chessengine.Move(gs.board, o=(col, row), t=(col + dx[i], row + dy[i])))
    Castle = getBlackCastle(gs)
    if (Castle == True):
        ValidKingMoves.append(chessengine.Move(gs.board, o=(col, row), t=(6, 7), castle=True))
    bigCastle = getbigBlackCastle(gs)
    if (bigCastle):
        ValidKingMoves.append(chessengine.Move(gs.board, o=(col, row), t=(2, 7), bigcastle=True))
    return ValidKingMoves

def getWhiteCastle(gs):
    if(gs.Whitecastle == True):
        if(gs.board[7][6] == "--"):
            if (gs.board[7][5] == "--"):
                if(NotControled(gs, [(4, 7), (5, 7), (6, 7)])):
                    return True
    return False

def getbigWhiteCastle(gs):
    if (gs.Whitebigcastle == True):
        if (gs.board[7][3] == "--"):
            if (gs.board[7][2] == "--"):
                if (gs.board[7][1] == "--"):
                    if (NotControled(gs, [(4, 7), (3, 7), (2, 7)])):
                        return True
    return False


def getBlackCastle(gs):
    if(gs.Blackcastle == True):
        if(gs.board[0][6] == "--"):
            if (gs.board[0][5] == "--"):
                if(NotControled(gs, [(4, 0), (5, 0), (6, 0)])):
                    return True
    return False

def getbigBlackCastle(gs):
    if (gs.Blackbigcastle == True):
        if (gs.board[0][3] == "--"):
            if (gs.board[0][2] == "--"):
                if (gs.board[0][1] == "--"):
                    if (NotControled(gs, [(4, 0), (3, 0), (2, 0)])):
                        return True
    return False

def NotControled(gs, squares):
    gs.Whitetomove = not gs.Whitetomove
    ValidMoves = CreateValidMovesNC(gs)
    gs.Whitetomove = not gs.Whitetomove
    n = len(ValidMoves)
    for i in range(0, n):
        print(ValidMoves[i].Notation)
        for c in squares:
            if(ValidMoves[i].to == c):
                return False
    return True


def ValidWhiteKingNC(gs, row, col):
    ValidKingMoves = []
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(0, 8):
        if ((0 <= col + dx[i]) and (col + dx[i] < 8) and (0 <= row + dy[i]) and (row + dy[i] < 8)):
            if ((gs.board[row + dy[i]][col + dx[i]][0] == "-") or (gs.board[row + dy[i]][col + dx[i]][0] == "b")):
                ValidKingMoves.append(chessengine.Move(gs.board, o=(col, row), t=(col + dx[i], row + dy[i])))
    return ValidKingMoves


def ValidBlackKingNC(gs, row, col):
    ValidKingMoves = []
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(0, 8):
        if ((0 <= col + dx[i]) and (col + dx[i] < 8) and (0 <= row + dy[i]) and (row + dy[i] < 8)):
            if ((gs.board[row + dy[i]][col + dx[i]][0] == "-") or (gs.board[row + dy[i]][col + dx[i]][0] == "w")):
                ValidKingMoves.append(chessengine.Move(gs.board, o=(col, row), t=(col + dx[i], row + dy[i])))
    return ValidKingMoves


def CreateValidMovesNC(gs):
    ValidMoves = []
    color = "w" if gs.Whitetomove else "b"
    for r in range(chessmain.DIMENSION):
        for c in range(chessmain.DIMENSION):
            if(color == gs.board[r][c][0]):
                ValidMoves += valid.func_dictioNC[gs.board[r][c][1]](gs, (c, r), color)
    return ValidMoves