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
    clock = pygame.time.Clock()

    z = 0
    # Event loop
    while True:
        clock.tick(60)
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.Quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #pygame.draw.line(screen, BLACK, last_pos, pygame.mouse.get_pos())
                z = 1
            elif event.type == MOUSEBUTTONUP:
                z = 0

            if z == 1:
                pygame.draw.line(screen, BLACK, last_pos, pygame.mouse.get_pos())
        pygame.display.update()
if __name__ == '__main__': main()
