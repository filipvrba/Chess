"""
This is our main driver file. It will be responsible for handling user
input and displaing the current GameState object.
"""

import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512  # 400 is another option
DIMENSION = 8  # dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animations later on
IMAGES = {}


def load_images():
    """
    Initialize a global dictionary of images. This will be called exactly
    once in the main.
    """

    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK",
              "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        # Note: we can access an image by saying 'IMAGES['wp']'
        IMAGES[piece] = p.transform.scale(
                p.image.load(f'images/{piece}.png'), (SQ_SIZE, SQ_SIZE))


def main():
    """
    The main driver for our code. This will handle user input and updating
    the graphics.
    """

    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.GameState()
    load_images()  # only do this once, before the while loop

    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def draw_game_state(screen, gs):
    """
    Responsible for all the graphics within a current game state.
    """

    draw_board(screen)  # draw squares on the board
    # Add in piece highlighting or move sugestions (later)
    draw_pieces(screen, gs.board)  # draw pieces on top of those squares


def draw_board(screen):
    """
    Draw the squares on the board.
    The top left square is always light.
    """

    colors = [p.Color('white'), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE,
                    SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, board):
    """
    Draw the pieces on the board using the current GameState.board
    """

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # not empty square
                screen.blit(IMAGES[piece],
                        p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE,
                        SQ_SIZE))
                

if __name__ == '__main__':
    main()