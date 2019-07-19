"""
pyxie game engine
Tutorial03

class DynamicBox
"""

from pyxie.apputil import graphicsHelper
import pyvmath as vmath
from Box2D.b2 import (world, polygonShape, staticBody, dynamicBody)

class DynamicBox:
    def __init__(self, world, showcase, pos, size, angle=0, static=False):

        if static:
            self.body = world.CreateStaticBody(position=pos, shapes=polygonShape(box=size), )
        else:
            self.body = world.CreateDynamicBody(position=pos, angle=angle)
            self.body.CreatePolygonFixture(box=size, density=1, friction=0.3)

        points = self.body.fixtures[0].shape.vertices
        index = (0,1,3,1,2,3)
        self.figure = graphicsHelper.createMesh(points, index)
        showcase.add(self.figure)

    def update(self):
        self.figure.position = (self.body.transform.position.x, self.body.transform.position.y)
        self.figure.rotation = vmath.quat_rotationZ(self.body.transform.angle)
