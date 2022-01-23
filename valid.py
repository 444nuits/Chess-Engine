"""
File responsible for generating the valid moves list each turn
"""


from copy import copy
import chessmain
import chessengine
import validrook
import validpawn
import validknight
import validking
import validbishop
import validqueen

def isValidMove(move, gs):
    transNotation(move)
    ValidMoves = CreateValidMoves(gs)
    if(ValidMoves == []):
        if(isMate(gs)):
            return (False, "Mate")
        else :
            return (False, "Pat")
    if(NoMoves(ValidMoves)):
        if (isMate(gs)):
            return (False, "Mate")
        else:
            return (False, "Pat")
    n = len(ValidMoves)
    for i in range(n):
        testedmove = ValidMoves[i]
        if(move.Notation == testedmove.Notation):
            if(testedmove.enpassant == True):
                move.enpassant = True
            return (True, "valid")
    return (False, "invalid")

def isMate(gs):
    if(gs.Whitetomove):
        if(InCheck(gs, gs.WhiteKing)):
            return True
    else :
        if(InCheck(gs, gs.BlackKing)):
            return True
    return False

def InCheck(gs, king):
    gs.Whitetomove = not gs.Whitetomove
    ValidMoves = validking.CreateValidMovesNC(gs)
    gs.Whitetomove = not gs.Whitetomove
    n = len(ValidMoves)
    for i in range(0, n):
        if(ValidMoves[i].to == king):
            return True
    return False

def NoMoves(moves):
    n = len(moves)
    for i in range(0, n):
        if(moves[i].Notation[-1] != "X"):
            return False
    return True

def transNotation(move):
    if(isCastle(move)):
        move.castle = True
        move.Notation = "O-O"
    if(isbigCastle(move)):
        move.bigcastle = True
        move.Notation = "O-O-O"

def isCastle(move):
    if(move.piecemoved[1] == "K"):
        if(move.origin == (4, 7) and move.to == (6, 7)):
            return True
        if (move.origin == (4, 0) and move.to == (6, 0)):
            return True

def isbigCastle(move):
    if (move.piecemoved[1] == "K"):
        if (move.origin == (4, 7) and move.to == (2, 7)):
            return True
        if (move.origin == (4, 0) and move.to == (2, 0)):
            return True

def ValidRook(gs, case, color):
    return validrook.ValidWhiteRook(gs, case[1], case[0]) if (color == "w") else validrook.ValidBlackRook(gs, case[1], case[0])

def ValidKnight(gs, case, color):
    return validknight.ValidWhiteKnight(gs, case[1], case[0]) if (color == "w") else validknight.ValidBlackKnight(gs, case[1], case[0])

def ValidBishop(gs, case, color):
    return validbishop.ValidWhiteBishop(gs, case[1], case[0]) if (color == "w") else validbishop.ValidBlackBishop(gs, case[1], case[0])

def ValidQueen(gs, case, color):
    return validqueen.ValidWhiteQueen(gs, case[1], case[0]) if (color == "w") else validqueen.ValidBlackQueen(gs, case[1], case[0])

def ValidKing(gs, case, color):
    return validking.ValidWhiteKing(gs, case[1], case[0]) if (color == "w") else validking.ValidBlackKing(gs, case[1], case[0])

def ValidPawn(gs, case, color):
    return validpawn.ValidWhitePawn(gs, case[1], case[0]) if (color == "w") else validpawn.ValidBlackPawn(gs, case[1], case[0])


func_dictio = {"R": ValidRook, "N": ValidKnight, "B": ValidBishop,
               "Q": ValidQueen, "K": ValidKing, "p": ValidPawn}


def ValidKingNC(gs, case, color): #No castle to avoir recursive problemes when checking if castle is allowed
    return validking.ValidWhiteKingNC(gs, case[1], case[0]) if (color == "w") else validking.ValidBlackKingNC(gs, case[1], case[0])

func_dictioNC = {"R" : ValidRook, "N" : ValidKnight, "B" : ValidBishop,
                 "Q" : ValidQueen, "K" : ValidKingNC, "p": ValidPawn}

def CreateValidMoves(gs):
    ValidMoves = []
    color = "w" if gs.Whitetomove else "b"
    for r in range(chessmain.DIMENSION):
        for c in range(chessmain.DIMENSION):
            if(color == gs.board[r][c][0]):
                ValidMoves += func_dictio[gs.board[r][c][1]](gs, (c, r), color)
    isCheck(ValidMoves, gs)
    return ValidMoves


def isCheck(moves, gs):
    for i in range(0, len(moves)):
        board, whiteking, blackking = copy(gs.board), gs.WhiteKing, gs.BlackKing
        gsbis= chessengine.GameState()
        gsbis.board, gsbis.WhiteKing, gsbis.BlackKing = board, whiteking, blackking
        gsbis.movelog = copy(gs.movelog)
        apply(moves[i], gsbis) #Applique le coup dans un autre echiquier non lié, d'ou la fonction copy
        if(gs.Whitetomove):
            if(not validking.NotControled(gsbis, [gsbis.WhiteKing])): #verifie que le roi blanc n'est pas en echec
                moves[i].Notation += "X"
        else :
            if (not validking.NotControled(gsbis, [gsbis.BlackKing])): #verifie que le roi noir n'est pas en echec
                moves[i].Notation += "X"



def apply(move, gs):
    board = gs.board
    board[move.origin[1]][move.origin[0]] = "--"
    board[move.to[1]][move.to[0]] = move.piecemoved
    if (move.bigcastle == True):
        board[move.origin[1]][3] = board[move.origin[1]][0]
        board[move.origin[1]][0] = "--"
    if (move.castle == True):
        board[move.origin[1]][5] = board[move.origin[1]][7]
        board[move.origin[1]][7] = "--"
    if (move.enpassant == True):
        board[move.origin[1]][move.to[0]] = "--"
    if (move.piecemoved == "wK"):
        gs.WhiteKing = (move.to[0], move.to[1])
    if (move.piecemoved == "bK"):
        gs.BlackKing = (move.to[0], move.to[1])
    gs.Whitetomove = not gs.Whitetomove
    gs.movelog.append(move)
