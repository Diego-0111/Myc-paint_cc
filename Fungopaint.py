import pygame
from pygame.locals import *

def main():
    # Initialise screen
    pygame.init()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    screen = pygame.display.set_mode((800, 600), 0, 32)
    canvas = screen.copy
    pygame.display.set_caption('Fungopaint')
    screen.fill(WHITE)

    mouse_posistion = (0,0)
    mouse = pygame.mouse
    drawing = False
    last_pos = pygame.mouse.get_pos()

    # Event loop
    while True:
        left_pressed = mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.Quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.line(screen, BLACK, last_pos, pygame.mouse.get_pos(), 1)
        pygame.display.update()

if __name__ == '__main__': main()
