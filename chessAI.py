#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 16:12:33 2022

@author: brieuc

Searches the move tree for automatically playing, evaluates the position
"""

#The tree search only promotes to queen

import chessmain
import chessengine
import valid
import copy as c


class Node:
    def __init__(self, children=[], position = None):
        self.children = children
        self.position = position
        self.value = evaluate(position)
        self.player = position.Whitetomove

def evaluate(gs):
    Mat = Material(gs)
    return Mat


def alphabetasearch(node, alpha, beta, depth):
    print(depth)
    BuildChildrenNodes(node)
    if(not depth):
        return node.value
    if(not node.player):
        v = -1000
        for childnode in node.children:
            v = min(v, alphabetasearch(childnode, alpha, beta, depth-1))
            if(alpha >= v):
                return v
            beta = min(beta, v)
    else :
        v = 1000
        for childnode in node.children:
            v = max(v, alphabetasearch(childnode, alpha, beta, depth-1))
            if(beta <= v):
                return v
            alpha = max(alpha, v)
    return v

Matdictio = {"wp": 1, "wR": 5, "wN": 3, "wB": 3, "wQ": 9, "wK": 0,
             "bp": -1, "bR": -5, "bN": -3, "bB": -3, "bQ": -9,"bK": 0, "--": 0}


def Material(gs):
    mat=0
    for r in range(chessmain.DIMENSION):
        for c in range(chessmain.DIMENSION):
            mat += Matdictio[gs.board[r][c]]
    return mat


def BuildChildrenNodes(node):
    Moves = valid.CreateValidMoves(node.position)
    for move in Moves:
        gs = CreateGameStateCopy(node)
        ApplyMoveBoard(gs, move)
        print(gs.movelog[0].Notation)
        childnode = Node(position=gs)
        print(childnode.position.movelog[0].Notation)
        node.children.append(childnode)


def ApplyMoveBoard(gs, move):
    chessengine.castles(move, gs)
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
        if (gs.Whitetomove):
            move.piececaptured = "bp"
        else:
            move.piececaptured = "wp"
    if (move.piecemoved == "wK"):
        gs.WhiteKing = (move.to[0], move.to[1])
    if (move.piecemoved == "bK"):
        gs.BlackKing = (move.to[0], move.to[1])
    gs.movelog.append(move)
    gs.Whitetomove = not gs.Whitetomove
    if (move.piecemoved[1] == "p" and (move.to[1] == 0 or move.to[1] == 7)):
        board[move.to[1]][move.to[0]] = board[move.to[1]][move.to[0]][0] + "Q"


def CreateGameStateCopy(node):
    gs = chessengine.GameState()
    gs.Whitetomove = node.position.Whitetomove
    gs.Blackbigcastle = node.position.Blackbigcastle
    gs.Blackcastle = node.position.Blackcastle
    gs.Whitebigcastle = node.position.Whitebigcastle
    gs.Whitecastle = node.position.Whitecastle
    gs.BlackKing = node.position.BlackKing
    gs.WhiteKing = node.position.WhiteKing
    gs.board = c.copy(node.position.board)
    return gs


def play(gs):
    rootnode = Node(position=gs)
    BuildChildrenNodes(rootnode)
    for i in range(len(rootnode.children)):
        print(rootnode.children[i])
        print(rootnode.children[i].position)
        print((rootnode.children[i]).position.movelog[0])
        print((rootnode.children[i]).position.movelog[0].Notation)
    idx = 0
    initwhiteeval = -1000
    initblackeval = 1000
    if(gs.Whitetomove):
        for i in range(len(rootnode.children)):
            eval = alphabetasearch(rootnode.children[i], -1000, 1000, 5)
            if (eval > initwhiteeval):
                initwhiteeval = eval
                idx = i
    else :
        for i in range(len(rootnode.children)):
            eval = alphabetasearch(rootnode.children[i], -1000, 1000, 5)
            if (eval < initblackeval):
                initblackeval = eval
                idx = i
    move = rootnode.children[idx].position.movelog.pop()
    print(move.Notation)
    return move