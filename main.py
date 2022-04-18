import pygame
from pygame.locals import QUIT

from func_handler import WIDTH, HEIGHT

pygame.init()
fps = 60
fps_clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    """The main loop"""
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == '__main__':
    main()
