import pygame
from pygame.locals import QUIT

from classes import Point, Circle
from func_handler import WIDTH, HEIGHT, get_lines_from_fn

pygame.init()
fps = 60
fps_clock = pygame.time.Clock()


def draw_lines(screen, lines: list[tuple[Point, Point]]):
    """Draws the lines got from marching squares"""
    color = (255, 0, 0)
    for t in lines:
        p1, p2 = t
        pygame.draw.line(screen, color, (p1.x, p1.y), (p2.x, p2.y))


def main():
    """The main loop"""
    # fn = lambda x, y: 90 / ((x ** 2 + y ** 2) ** .5)
    # fn2 = lambda x, y: 70 / (((x - 300) ** 2 + y ** 2) ** .5)
    # fn3 = lambda x, y: fn(x, y) + fn2(x, y)
    c = Circle(20, Point(0, 0), Point(20, 20))
    c2 = Circle(15, Point(0, 0), Point(-10, 5))
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        c.update(WIDTH, HEIGHT)
        c2.update(WIDTH, HEIGHT)
        lines = get_lines_from_fn(lambda x, y: c.draw_function(x, y) + c2.draw_function(x, y))
        draw_lines(screen, lines)
        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == '__main__':
    main()
