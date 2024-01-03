from OpenGL.GL import *


class CameraClass:
    _position = [0,0,0]
    _rotation = [0,0,0,0]
    _childTo = []

    def __init__(self, position, childTo):
        self._position = position
        self._childTo = childTo

    # Focus point of where looking at, Z is the fov and x, y are the height
    def translate(self, x, y, z):
        glTranslatef(x, y, z)
        self._position[0] += x
        self._position[1] += y
        self._position[2] += z

    def rotation(self, angle, x, y, z):
        glRotatef(angle, x, y, z)
        self._rotation[0] += angle
        self._rotation[1] += x
        self._rotation[2] += y
        self._rotation[3] += z

    def getPosition(self):
        return self._position

    def getRotation(self):
        return self._rotation
