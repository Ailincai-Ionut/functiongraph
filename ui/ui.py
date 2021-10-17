import sys
import pygame
import math

pygame.init()

size = width, height = 640, 480

ox = -10, 10
oy = -10, 10
origin = [size[0] / 2, size[1] / 2]
px_per_unitx = size[0] / (ox[1] - ox[0])
px_per_unity = size[1] / (oy[1] - oy[0])

screen = pygame.display.set_mode(size)


def draw_axes(screen):
    for i in range(0, ox[1] - ox[0] + 1, 1):
        pygame.draw.lines(screen, (0, 0, 0), True, [
                          (i * px_per_unitx, origin[1] - 5),  (i * px_per_unitx, origin[1] + 5)])
    for i in range(0, oy[1] - oy[0] + 1, 1):
        pygame.draw.lines(screen, (0, 0, 0), True, [
                          (origin[0] - 5, i * px_per_unity),  (origin[0] + 5, i * px_per_unity)])
    pygame.draw.lines(screen, (0, 0, 0), True, [
                      (0, origin[1]),  (size[0], origin[1])])
    pygame.draw.lines(screen, (0, 0, 0), True, [
                      (origin[0], 0),  (origin[0], size[1])])


def f(x):
    return math.sqrt(abs(1 - x**2))


while 1:
    screen.fill((128, 128, 128))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    draw_axes(screen)
    p = [0, int((f(0) - oy[0]) / (oy[1] - oy[0]) * size[1])]
    i = ox[0]
    while i < ox[1]:
        r = (i - ox[0]) / (ox[1] - ox[0])
        rf = (f(i) - oy[0]) / (oy[1] - oy[0])
        print((int(r * size[0]), int(rf * size[1])), i, rf, r)
        new_p = [int(r * size[0]), int(rf * size[1])]
        pygame.draw.line(screen, (0, 0, 0), p, new_p)
        p = new_p.copy()
        i += (ox[1] - ox[0]) / size[0]
    pygame.display.flip()
