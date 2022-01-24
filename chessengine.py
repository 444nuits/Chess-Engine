#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 16:12:33 2022

@author: brieuc

Deals with the state of the board
"""

import numpy as np
import pygame as p
import valid


class GameState:
    def __init__(self):
        self.board = np.array([
            np.array(["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]),
            np.array(["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"]),
            np.array(["--", "--", "--", "--", "--", "--", "--", "--"]),
            np.array(["--", "--", "--", "--", "--", "--", "--", "--"]),
            np.array(["--", "--", "--", "--", "--", "--", "--", "--"]),
            np.array(["--", "--", "--", "--", "--", "--", "--", "--"]),
            np.array(["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"]),
            np.array(["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"])
        ])
        self.Whitetomove = True
        self.movelog = []
        self.Blackbigcastle = True
        self.Blackcastle = True
        self.Whitebigcastle = True
        self.Whitecastle = True
        self.BlackKing = (4, 0)
        self.WhiteKing = (4, 7)

class Move:
    ranksToRows = {"1" : 7, "2" : 6, "3" : 5, "4" : 4,
                   "5" : 3, "6" : 2, "7" : 1, "8" : 0,}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7, }
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, board, o=(), t=(), enpassant = False, castle=False, bigcastle=False):
        self.origin = o
        self.to = t
        self.who = True
        self.piecemoved = board[o[1]][o[0]]
        self.piececaptured = board[t[1]][t[0]]
        self.castle = castle
        self.bigcastle = bigcastle
        self.enpassant = enpassant
        self.Notation = self.getChessNotation()


    def getChessNotation(self):
        Not = ""
        if(self.castle == True):
            Not += "O-O"
            return Not
        if(self.bigcastle == True):
            Not += "O-O-O"
            return Not
        if(self.piecemoved[1] != "p"):
            Not += self.piecemoved[1]
        if(self.piecemoved[1] == "p") :
            if(self.origin[0] != self.to[0]):
                Not += self.colsToFiles[self.origin[0]]
                if(self.piececaptured == "--"):
                    Not += "x"
        if(self.piececaptured != "--"):
            Not += "x"
        Not += self.colsToFiles[self.to[0]]
        Not += self.rowsToRanks[self.to[1]]
        return Not


def applyMove(clicks, gs):
    move = Move(gs.board, o=clicks[0], t=clicks[1])
    board = gs.board
    (bool, state) = valid.isValidMove(move, gs)
    if ((gs.Whitetomove and move.piecemoved[0] == "w") or (not gs.Whitetomove and move.piecemoved[0] == "b")):
        if(bool):
            print("Valid Move,", "black" if gs.Whitetomove else "white", "to play")
            castles(move, gs)
            board[move.origin[1]][move.origin[0]] = "--"
            board[move.to[1]][move.to[0]] = move.piecemoved
            if(move.bigcastle == True):
                board[move.origin[1]][3] = board[move.origin[1]][0]
                board[move.origin[1]][0] = "--"
            if(move.castle == True):
                board[move.origin[1]][5] = board[move.origin[1]][7]
                board[move.origin[1]][7] = "--"
            if(move.enpassant == True):
                board[move.origin[1]][move.to[0]] = "--"
                if(gs.Whitetomove):
                    move.piececaptured = "bp"
                else :
                    move.piececaptured = "wp"
            if(move.piecemoved == "wK"):
                gs.WhiteKing = (move.to[0], move.to[1])
            if (move.piecemoved == "bK"):
                gs.BlackKing = (move.to[0], move.to[1])
            gs.movelog.append(move)
            gs.Whitetomove = not gs.Whitetomove
            if(move.piecemoved[1] == "p"):
                if(move.to[1] == 0 or move.to[1] == 7):
                    asking = True
                    while asking:
                        for e in p.event.get():
                            if(e.type == p.KEYDOWN):
                                if(e.key == p.K_r):
                                    board[move.to[1]][move.to[0]] = board[move.to[1]][move.to[0]][0] + "R"
                                    asking = False
                                if (e.key == p.K_q):
                                    board[move.to[1]][move.to[0]] = board[move.to[1]][move.to[0]][0] + "Q"
                                    asking = False
                                if (e.key == p.K_b):
                                    board[move.to[1]][move.to[0]] = board[move.to[1]][move.to[0]][0] + "B"
                                    asking = False
                                if (e.key == p.K_n):
                                    board[move.to[1]][move.to[0]] = board[move.to[1]][move.to[0]][0] + "N"
                                    asking = False
    else :
        if(state == "Mate"):
            print("Mate")
        if(state == "Pat"):
            print("pat")
        if(state == "invalid"):
            if(gs.Whitetomove):
                print("Invalid Move, white try another")
            else :
                print("Invalid Move, black try another")
    #print(move.getChessNotation())

def UndoMove(gs):
    if(len(gs.movelog)):
        move = gs.movelog.pop()
        gs.board[move.to[1]][move.to[0]] = move.piececaptured
        gs.board[move.origin[1]][move.origin[0]] = move.piecemoved
        gs.Whitetomove = not gs.Whitetomove

def castles(move, gs):
    if(move.origin[1] == 7):
        if(move.piecemoved[1] == "K"):
            gs.Whitebigcastle = False
            gs.Whitecastle = False
        if(move.piecemoved[1] == "R"):
            if(move.origin[0] == 0):
                gs.Whitebigcastle = False
            if(move.origin[0] == 7):
                gs.Whitecastle = False
    if (move.origin[1] == 0):
        if (move.piecemoved[1] == "K"):
            gs.Blackbigcastle = False
            gs.Blackcastle = False
        if (move.piecemoved[1] == "R"):
            if (move.origin[0] == 0):
                gs.Blackbigcastle = False
            if (move.origin[0] == 7):
                gs.Blackcastle = False

