import pygame
from pygame.locals import *
import math
import sys

from ui.graph import *
'''
pygame.init()
size = width, height = 1280, 640
screen = pygame.display.set_mode(size)

game = Graph(screen, [100, 100], [600, 500],
             [Function("sqrt(x,0)", (255, 0, 0))])
game2 = Graph(screen, [601, 100], [1100, 500], [
    Function("sin(x,0)", (255, 0, 0)),
    Function("cos(x,0)", (0, 255, 0)),
    Function("tan(x,0)", (0, 0, 255))
])

windows = [
    Graph(screen, [100, 100], [600, 500], []),
    Graph(screen, [601, 100], [1100, 500], [
        Function("sin(x,0)", 1, (255, 0, 0)),
        Function("cos(x,0)", 1, (0, 255, 0)),
        Function("tan(x,0)", 1, (0, 0, 255))
    ])
]


def isInWindow(mouse, window):
    start, size = window.get_coord()
    if mouse[0] > start[0] and mouse[0] < start[0] + size[0] and mouse[
            1] > start[1] and mouse[1] < start[1] + size[1]:
        return True
    return False


def f(l):
    print(l)
    return l


func = Function("lol", f)

print(func.get_point_at(1))

pressed = False
while True:
    inp = []
    print(pygame.mouse.get_rel())
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[K_SPACE]:
                windows[1].set_size([600, 510])
        if e.type == pygame.MOUSEBUTTONUP:
            pressed = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            pressed = True
    for w in windows:
        if isInWindow(pygame.mouse.get_pos(), w):
            if pygame.mouse.get_pressed()[0] and pressed:
                pressed = True
                start = w.get_start()
                rel = pygame.mouse.get_rel()
                w.set_start([start[0] + rel[0], start[1] + rel[1]])
            w.run(screen, [pygame.key.get_pressed(), pygame.mouse.get_pos()])
        else:
            w.run(screen, [])
    pygame.display.flip()
'''
