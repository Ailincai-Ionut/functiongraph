import pygame
import sys
from pygame.locals import *

from expressions.func import *


class Function():
    def __init__(self, text_function, f=None, color=(0, 0, 0)):
        self.expression = text_function
        self.color = color
        self.points = []
        self.f = f

    def update_points(self, interval):
        return self.points

    def get_point_at(self, x):
        return self.f(x)

    def set_func(self, f):
        self.f = f


class Graph():
    def __init__(self, surface, start, end, functions=[]):
        self.screen = surface
        self.start = start
        self.size = [end[0] - start[0], end[1] - start[1]]
        self.ox = [-10, 10]
        self.oy = [-10, 10]
        self.origin = [self.size[0] / 2, self.size[1] / 2]
        self.px_per_unitx = self.size[0] / (self.ox[1] - self.ox[0])
        self.px_per_unity = self.size[1] / (self.oy[1] - self.oy[0])
        self.functions = functions
        self.points = []
        self.update()

    def draw_axes(self):
        #This is utterly shit, fix this pls
        '''
        for i in range(0, int(self.ox[1] - self.ox[0] + 1), 1):
            pygame.draw.lines(self.screen, (0, 0, 0), True,
                              [(i * self.px_per_unitx, self.origin[1] - 5),
                               (i * self.px_per_unitx, self.origin[1] + 5)])
        for i in range(0, int(self.oy[1] - self.oy[0] + 1), 1):
            pygame.draw.lines(self.screen, (0, 0, 0), True,
                              [(self.origin[0] - 5, i * self.px_per_unity),
                               (self.origin[0] + 5, i * self.px_per_unity)])
        '''
        #The ox axis
        if self.oy[0] < 0 and self.oy[1] > 0:
            self.line((0, 0, 0), (0, self.origin[1]),
                      (self.size[0], self.origin[1]))
        if self.ox[0] < 0 and self.ox[1] > 0:
            self.line((0, 0, 0), (self.origin[0], 0),
                      (self.origin[0], self.size[1]))

    def update(self):
        increment = (self.ox[1] - self.ox[0]) / self.size[0]
        for f in self.functions:
            f.points = evaluate(f.expression,
                                [self.ox[0], self.ox[1], increment])
        self.adjust_origin()

    def input(self, keys, mouse):
        if keys != None:
            if keys[K_LEFT]:
                self.ox[0] -= 0.33
                self.ox[1] -= 0.33
            if keys[K_RIGHT]:
                self.ox[0] += 0.33
                self.ox[1] += 0.33
            if keys[K_UP]:
                self.oy[0] += 0.33
                self.oy[1] += 0.33
            if keys[K_DOWN]:
                self.oy[0] -= 0.33
                self.oy[1] -= 0.33
            if keys[K_SPACE]:
                self.oy[0] += 0.33
                self.oy[1] -= 0.33
                self.ox[0] += 0.33
                self.ox[1] -= 0.33
        self.adjust_origin()
        self.update()

    def dist(self, p1=[], p2=[]):
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    def limit_line(self, s1, f1, s2, f2):
        '''
        This function gets the point intersected by the two lines
        formed by the points
        #We will use a complicated formula
        #link:https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line
        '''
        d = (s1[0] - f1[0]) * (s2[1] - f2[1]) - (s1[1] - f1[1]) * (s2[0] -
                                                                   f2[0])
        if d == 0:
            #You need to study what happens when d -> 0
            return f1
        xd = (s1[0] * f1[1] - s1[1] * f1[0]) * (s2[0] - f2[0]) - (
            s1[0] - f1[0]) * (s2[0] * f2[1] - s2[1] * f2[0])
        yd = (s1[0] * f1[1] - s1[1] * f1[0]) * (s2[1] - f2[1]) - (
            s1[1] - f1[1]) * (s2[0] * f2[1] - s2[1] * f2[0])
        return [int(xd / d), int(yd / d)]

    def line(self, color, s, f):
        #TODO: It needs to draw the line until the margin
        if (s[1] > self.size[1] and f[1] > self.size[1]) or (s[1] < 0
                                                             and f[1] < 0):
            return
        if s[1] > self.size[1]:
            s = self.limit_line(s, f, [s[0], self.size[1]],
                                [f[0], self.size[1]])
        elif s[1] < 0:
            s = self.limit_line(s, f, [s[0], 0], [f[0], 0])
        elif f[1] > self.size[1]:
            f = self.limit_line(s, f, [s[0], self.size[1]],
                                [f[0], self.size[1]])
        elif f[1] < 0:
            f = self.limit_line(s, f, [s[0], 0], [f[0], 0])
        pygame.draw.lines(self.screen, color, True,
                          [(self.start[0] + s[0], self.start[1] + s[1]),
                           (self.start[0] + f[0], self.start[1] + f[1])])

    def draw(self):
        self.screen.fill((128, 128, 128),
                         Rect(self.start[0], self.start[1], self.size[0],
                              self.size[1]))
        self.draw_axes()
        for f in self.functions:
            self.draw_func(f)
        pygame.draw.rect(
            self.screen, (0, 0, 0),
            Rect(self.start[0], self.start[1], self.size[0], self.size[1]), 2)

    def draw_func(self, f):
        '''
        This algorithm is efficient but very buggy
        Its needs f.points to be a list of points [x,y] so if used modify the
            get_interval_value() function from func.py to return such pairs'''
        if f.points != []:
            increment = (self.ox[1] - self.ox[0]) / self.size[0]
            p = [
                int(((f.points[0][0] - self.ox[0]) /
                     (self.ox[1] - self.ox[0])) * self.size[0]),
                int((f.points[0][1] - self.oy[0]) / (self.oy[0] - self.oy[1]) *
                    self.size[1])
            ]
            for point in f.points:
                rf = (point[1] - self.oy[0]) / (self.oy[1] - self.oy[0])
                r = (point[0] - self.ox[0]) / (self.ox[1] - self.ox[0])
                new_p = [int(r * self.size[0]), int((1 - rf) * self.size[1])]
                if self.dist(p,
                             new_p) < 1000:  #this hard-coded value is not good
                    self.line(f.color, p, new_p)
                p = new_p.copy()

    def run(self, input):
        '''
        the input needs to be a list with 2 elements: the keys and mouse
        '''
        if len(input) == 2:
            self.input(input[0], input[1])
        self.draw()

    def get_coord(self):
        return [self.start, self.size]

    def set_size(self, size):
        self.size = size
        self.adjust_origin()

    def get_start(self):
        return self.start

    def set_start(self, start):
        self.start = start

    def adjust_origin(self):
        # the absolute lenght of the ox axis displayed
        lenghtx = self.ox[1] - self.ox[0]
        # the ratio between the whole lenght of ox and the lenght of the ox'
        rx = abs(self.ox[0]) / lenghtx
        self.origin[0] = rx * self.size[0]
        # analog for oy
        lenghty = self.oy[1] - self.oy[0]
        ry = abs(self.oy[0]) / lenghty
        self.origin[1] = (1 - ry) * self.size[1]
        self.px_per_unitx = self.size[0] / (self.ox[1] - self.ox[0])
        self.px_per_unity = self.size[1] / (self.oy[1] - self.oy[0])
