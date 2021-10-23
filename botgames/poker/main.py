# modules
import sys
import pygame
from pygame.locals import *

# globals
FPS = 60
WINDOW_SIZE = (1200, 700)

# common objects
bg = pygame.image.load('resources/bg.png')

# menu objects
title = pygame.image.load('resources/title.png')

# game objects


# functions
def draw_text(content, size=32, pigment=(255, 255, 255), bold=False, italic=False):
    font = pygame.font.SysFont('Arial', size, bold=bold, italic=italic)
    text = font.render(content, True, pigment)
    return text


# screens
def menu_screen():
    # menu loop
    while True:
        screen.blit(bg, (0, 0))
        screen.blit(title, (300, 75))

        text_p1 = draw_text('J1:')
        screen.blit(text_p1, (400, 300))
        text_p2 = draw_text('J2:')
        screen.blit(text_p2, (400, 400))

        # event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            # here goes an event when the play button is clicked

        # refresh
        pygame.display.update()
        clock.tick(FPS)


def game_screen():
    # game loop
    while True:
        screen.blit(bg, (0, 0))

        # event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # refresh
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('Poker: Discord Edition')
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    
    # main loop
    while True:
        menu_screen()

        game_screen()
