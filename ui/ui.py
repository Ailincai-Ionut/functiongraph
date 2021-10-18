import pygame
from pygame.locals import *
import math

#from .funciongraph.expressions.func import *
import sys
if True:
    sys.path.append('../expressions')
    from func import *
from graph import *

pygame.init()
size = width, height = 1280, 640
screen = pygame.display.set_mode(size)

game = Graph(screen, [100, 100], [600, 500], [
    Function("sin(x,0)", (255, 0, 0)),
    Function("cos(x,0)", (0, 255, 0)),
    Function("tan(x,0)", (0, 0, 255))
])
game2 = Graph(screen, [601, 100], [1100, 500], [
    Function("x*sin(x,0)", (255, 0, 0)),
    Function("x*cos(x,0)", (0, 255, 0)),
    Function("x*tan(x,0)", (0, 0, 255))
])

while 1:
    inp = []
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            inp = [pygame.key.get_pressed(), [1]]

    game.run(screen, inp)
    game2.run(screen, inp)
    pygame.display.flip()
