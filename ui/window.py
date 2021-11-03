import pygame
import sys
from pygame.locals import *


class Button():
    def __init__(self, text, start, end):
        self.start = start
        self.size = [end[0] - start[0], end[1] - start[1]]

    def isOnButton(self, x, y):
        if x > self.start[0] and x < self.start[0] + self.size[
                0] and y > self.start[1] and y < self.start[1] + self.size[1]:
            return True
        return False


class Window():
    def __init__(self, surface, start, end):
        self.screen = surface
        self.start = start
        self.size = [end[0] - start[0], end[1] - start[1]]
        self.size_bar = [self.size[0], int(self.size[1] * 0.05)]

    def draw(self):
        self.screen.fill((128, 128, 128),
                         Rect(self.start[0], self.start[1], self.size[0],
                              self.size[1]))
        self.screen.fill((0, 0, 0),
                         Rect(self.start[0], self.start[1], self.size_bar[0],
                              self.size_bar[1]))

    def run(self, input):
        '''
        the input needs to be a list with 2 elements: the keys and mouse
        '''
        if len(input) == 2:
            self.input(input[0], input[1])
        self.draw()
