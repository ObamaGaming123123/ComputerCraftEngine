"""
Main.py
Created by James Thomson
Copyright (c)

Description : This program will run the program and display a graphical interface
"""

import pygame
from CubeClass import CubeClass
from CameraClass import CameraClass
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

_refreshRate = 10
__flipSwitch = False
__Objects = []
__Camera = CameraClass([0, 0, 0], None)
__AnimationEvents = []
__Debug = False


def InitialiseObjects():
    __Objects.append(CubeClass("1", 1, [0, 0, 0], (1, 0.5, 1, 0.5)))
    __Objects.append(CubeClass("1", 1, [1, 0, 0], (1, 0.5, 1, 0.5)))
    __Objects.append(CubeClass("1", 0.5, [0, 1, 0], (1, 0.5, 1, 0.5)))


if __name__ == '__main__':
    pygame.init()
    display = (1270, 720)

    # DoubleBuff is the switching method used also in DirectX
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # (FOV, (Aspect Ratio), znear, zfar)
    # znear and zfar is how far an object will disappear and reappear
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    __Camera.translate(0,0,-10)
    __Camera.rotation(45, 0, 0, 0)

    # This moves the camera to this perspective in the environment
    InitialiseObjects()
    __AnimationEvents.append([2, [1, 1, 0], 1])
    __AnimationEvents.append([2, [1, 0, 0], 1])

    while True:
        for event in pygame.event.get():
            if __Debug == True:
                print(event.type)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == 97:
                    __Camera.translate(0.2,0,0)
                elif event.key == 100:
                    __Camera.translate(-0.2, 0.0, 0)

        __Camera.rotation(1,0,0,1)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for obj in __Objects:
            obj.RenderCube()

        if __AnimationEvents:
            temp = __AnimationEvents.pop(0)
            if not __Objects[temp[0]].createAnimation(temp[1], temp[2]):
                __AnimationEvents.append(temp)

        pygame.display.flip()
        pygame.time.wait(_refreshRate)
