"""

Runs the game

"""

import pygame as p
import chessengine


WIDTH = HEIGHT = 512 #resolution images

DIMENSION = 8  # Echecs 8*8

CASE_SIZE = HEIGHT // DIMENSION

MAX_FPS = 15

IMAGES = {}

white = (230, 229, 205)
blue = (70, 104, 141)

'''
Load images, executed only once
'''

def ImagesLoad():
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bp", "wR", "wN", "wB", "wQ", "wK", "wp"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f'images/{piece}.png'), (CASE_SIZE, CASE_SIZE))


'''
fonction MAIN
'''

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    gs = chessengine.GameState()
    ImagesLoad()
    clicks = []
    case = ()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN :
                getMove(clicks, case, gs)
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def getMove(clicks, case, gs) :
    location = p.mouse.get_pos()
    col = location[0] // CASE_SIZE
    row = location[1] // CASE_SIZE
    if case == (col, row) :
        case = ()
    else :
        case = (col, row)
        clicks.append(case)
    if(len(clicks) == 2):
        chessengine.applyMove(clicks, gs)
        clicks.pop()
        clicks.pop()
        case = ()


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


def drawBoard(screen):
    colors = [white, blue]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
                p.draw.rect(screen, colors[((r+c)%2)], p.Rect(c*CASE_SIZE, r*CASE_SIZE, CASE_SIZE, CASE_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            if(board[c][r] != '--'):
                screen.blit(IMAGES[board[c][r]], (r*CASE_SIZE, c*CASE_SIZE))


if __name__ == "__main__":
    main()

