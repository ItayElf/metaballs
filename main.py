import pygame
from pygame.locals import QUIT

pygame.init()
fps = 60
fps_clock = pygame.time.Clock()
w, h = 640, 480
screen = pygame.display.set_mode((w, h))


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
