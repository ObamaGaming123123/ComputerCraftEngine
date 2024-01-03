import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class CubeClass:
    _cubePosition = []
    _cubeScale = []
    _cubeName = ""
    _color4fv = []
    _movementMultipliers = [0,0,0]
    _inAnimation = False

    # This is some vertices information on the first object
    __verticies = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )

    __edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7)
    )

    __surfaces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
    )

    def __init__(self, cubeName, cubeScale, cubePosition, color4fv):
        self._cubePosition = cubePosition
        self._cubeScale = cubeScale
        self._cubeName = cubeName
        self._color4fv = color4fv

    def createAnimation(self, newp, timeS):
        if not self._inAnimation:
            self._movementMultipliers[0] = ((newp[0] - self._cubePosition[0]) / timeS) / 100
            self._movementMultipliers[1] = ((newp[1] - self._cubePosition[1]) / timeS) / 100
            self._movementMultipliers[2] = ((newp[2] - self._cubePosition[2]) / timeS) / 100
            self._inAnimation = True

        # Warning: Can be skipped due to memory problems
        if round(abs(newp[0] - self._cubePosition[0]), 1) == 0 and round(abs(newp[1] - self._cubePosition[1]), 1) == 0 and round(abs(newp[2] - self._cubePosition[2]), 1) == 0:
            self._inAnimation = False
            return True
        else:
            self._cubePosition[0] += self._movementMultipliers[0]
            self._cubePosition[1] += self._movementMultipliers[1]
            self._cubePosition[2] += self._movementMultipliers[2]
            return False

    def RenderCube(self):
        glTranslate(self._cubePosition[0] * 2, self._cubePosition[1] * 2, self._cubePosition[2] * 2)
        glBegin(GL_QUADS)
        scaledVerticies = tuple(tuple(x * self._cubeScale for x in item) for item in self.__verticies)
        for surface in self.__surfaces:
            x = 0
            for vertex in surface:
                x += 1
                glColor4fv(self._color4fv)
                glVertex3fv(scaledVerticies[vertex])
        glEnd()

        # All GL statements must begin with an OPEN GL statement
        # GL_Lines is how we want to draw the data we give it, treating it as lines
        glBegin(GL_LINES)

        for edge in self.__edges:
            for vertex in edge:
                glColor4fv((0.0, 0.0, 0.0, 0.5))
                glVertex3fv(scaledVerticies[vertex])

        glEnd()
        glTranslate(self._cubePosition[0] * -2, self._cubePosition[1] * -2, self._cubePosition[2] * -2)

    def getCubePosition(self):
        return self._cubePosition

    def getCubeScale(self):
        return self._cubeScale

    def getCubeName(self):
        return self._cubeName
