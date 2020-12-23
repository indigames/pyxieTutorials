"""
indi game engine
Tutorial04

cam.py

TargetCamera class
"""
import igeCore as core
import igeVmath as vmath

class TargetCamera():

    def __init__(self):
        self.pos = vmath.vec3(0,0,5)
        self.height = 3.0
        self.targetHeighjt = 1.0
        self.camera = core.camera("cam01")
        self.camera.farPlane = 500.0

    def step(self, targetFigure):
        at = targetFigure.position

        dir = at - self.pos
        distance = vmath.length(dir)
        dir = vmath.normalize(dir)

        speed = 0.0
        if distance > 6.0:
           speed = (distance-6.0)*0.1
        elif distance < 4.0:
           speed = (distance-4.0)*0.1

        self.pos += dir*speed

        self.camera.target = at + vmath.vec3(0,self.targetHeighjt, 0)
        self.camera.position = self.pos + vmath.vec3(0,self.height, 0)

    def getWalkThroughMatrix(self):
        savePos = self.camera.position
        saveTarget = self.camera.target

        self.camera.position = (0, 0, 0)
        tmpPos  =  saveTarget - savePos
        self.camera.target = (tmpPos.x, 0, tmpPos.z)
        viewmat = self.camera.viewInverseMatrix

        self.camera.position = savePos
        self.camera.target = saveTarget
        return viewmat
