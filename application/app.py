import pygame
import sys
from pygame.locals import *
from ui import *
from ui.graph import *  #??
from ui.window import *  #??


class Application():
    def __init__(self, size, background_color, number_windows):
        self.size = size
        self.bgcolor = background_color
        self.nr_w = number_windows
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.windows = [
            Graph(self.screen, [100, 100], [600, 500],
                  [Function("sqrt(x^3-x^2,0)", 1, (255, 0, 0))]),
            Graph(self.screen, [601, 100], [1100, 500], [
                Function("sin(x,0)", 1, (255, 0, 0)),
                Function("cos(x,0)", 1, (0, 255, 0)),
                Function("tan(x,0)", 1, (0, 0, 255))
            ]),
            #Window(self.screen, [200, 200], [600, 500])
        ]

    def isInWindow(self, mouse, window):
        start, size = window.get_coord()
        if mouse[0] > start[0] and mouse[0] < start[0] + size[0] and mouse[
                1] > start[1] and mouse[1] < start[1] + size[1]:
            return True
        return False

    def run(self):
        pressed = False
        while True:
            inp = []
            self.screen.fill((255, 255, 255))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONUP:
                    pressed = False
                if e.type == pygame.MOUSEBUTTONDOWN:
                    pressed = True
            for w in self.windows:
                if self.isInWindow(pygame.mouse.get_pos(), w):
                    if pressed:
                        start = w.get_start()
                        rel = pygame.mouse.get_rel()
                        print(pressed, start, rel)
                        w.set_start([start[0] + rel[0], start[1] + rel[1]])
                        w.run(
                            [pygame.key.get_pressed(),
                             pygame.mouse.get_pos()])
                        continue
                    w.run([pygame.key.get_pressed(), pygame.mouse.get_pos()])
                w.run([])
            pygame.mouse.get_rel()
            pygame.display.flip()
