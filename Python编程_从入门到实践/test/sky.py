import sys
import pygame


def run_game():
    pygame.init()
    color = (0, 0, 255)
    screen = pygame.display.set_mode((1200, 800))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(color)
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
