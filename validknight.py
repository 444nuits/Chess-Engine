"""
Get Valid Knight Moves
"""

import chessengine

def ValidWhiteKnight(gs, row, col):
    ValidKnightMoves = []
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]
    for i in range(0, 8):
        if ((0 <= col + dx[i]) and (col + dx[i] < 8) and (0 <= row + dy[i]) and (row + dy[i] < 8)):
            if ((gs.board[row + dy[i]][col + dx[i]][0] == "-") or (gs.board[row + dy[i]][col + dx[i]][0] == "b")):
                ValidKnightMoves.append(chessengine.Move(gs.board, o=(col, row), t=(col + dx[i], row + dy[i])))
    return ValidKnightMoves

def ValidBlackKnight(gs, row, col):
    ValidKnightMoves = []
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]
    for i in range(0, 8):
        if ((0 <= col+dx[i]) and (col+dx[i] < 8) and (0 <= row+dy[i]) and (row+dy[i] < 8)):
            if ((gs.board[row+dy[i]][col+dx[i]][0] == "-") or (gs.board[row+dy[i]][col+dx[i]][0] == "w")):
                ValidKnightMoves.append(chessengine.Move(gs.board, o=(col, row), t=(col + dx[i], row + dy[i])))
    return ValidKnightMoves

