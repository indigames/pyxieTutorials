"""
indi game engine
Tutorial04

char.py

Character class
"""

import igeCore as core
from igeCore import devtool
from igeCore import apputil
import igeVmath as vmath
import os.path
import igeBullet
from utils import Utils

class Character():
    def __init__( self, world):
        self.figure = core.figure('capeMan')

        points = self.figure.getVertexElements('body',core.ATTRIBUTE_ID_POSITION, core.WorldSpace)
        shape = igeBullet.shape(igeBullet.CONVEX_HULL_SHAPE_PROXYTYPE, points = points)
        min, max = shape.getAabb()
        compound = igeBullet.shape(igeBullet.COMPOUND_SHAPE_PROXYTYPE)
        compound.addChildShape(shape, (0, -min[1],0), (0,0,0,1))
        self.body = igeBullet.rigidBody(compound,5,(0,0,0),(0,0,0,1))
        self.body.angularFactor = (0,1,0)
        world.add(self.body)
        #utl = Utils()
        #utl.AddShapeMesh(compound)

        points =  self.figure.getVertexElements('cape',core.ATTRIBUTE_ID_POSITION, space=core.WorldSpace)
        triangles =  self.figure.getTriangles('cape')
        self.soft = igeBullet.softBody(world, points, triangles)
        self.figure.killJointTransform('cape')
        self.figure.setMaterialRenderState('phong1', 'cull_face_enable', False)

        pos, _, _ = self.figure.getJoint('anchor1', core.WorldSpace)
        idx, _ = self.soft.findNearestNode(pos)
        self.soft.appendDeformableAnchor(idx, self.body)

        pos, _, _ = self.figure.getJoint('anchor2', core.WorldSpace)
        idx, _ = self.soft.findNearestNode(pos)
        self.soft.appendDeformableAnchor(idx, self.body)

        pos, _, _ = self.figure.getJoint('anchor3', core.WorldSpace)
        idx, _ = self.soft.findNearestNode(pos)
        self.soft.appendDeformableAnchor(idx, self.body)

        pos, _, _ = self.figure.getJoint('anchor4', core.WorldSpace)
        idx, _ = self.soft.findNearestNode(pos)
        self.soft.appendDeformableAnchor(idx, self.body)



    def step(self, moveVector):

        currentDir = vmath.mat33(self.figure.rotation).getCol(2)

        l = vmath.length(moveVector)
        if l > 10.0:
            gorlDir = vmath.normalize(moveVector)
            self.body.linearVelocity = gorlDir * 100.0 * core.getElapsedTime()
        else:
            gorlDir = currentDir
            self.body.linearVelocity = (0,0,0)

        self.body.angularVelocity = (0,0,0)
        r = vmath.dot(currentDir, gorlDir)
        if r < 0.99:
            n = vmath.cross(currentDir, gorlDir)
            self.body.angularVelocity = (0,n.y * 10.0,0)

        self.figure.rotation = self.body.rotation
        self.figure.position = self.body.position

        self.figure.setVertexElements('cape', core.ATTRIBUTE_ID_POSITION, self.soft.meshPositions())
        self.figure.setVertexElements('cape', core.ATTRIBUTE_ID_NORMAL, self.soft.meshNormals())

        #efig =Utils().GetFigure()
        #efig.setJoint(1, position=self.body.position, rotation=self.body.rotation)
