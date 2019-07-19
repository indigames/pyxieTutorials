"""
pyxie game engine
Tutorial04

char.py

Character class
"""
import pyxie
from pyxie import devtool
from pyxie import apputil
import pyvmath as vmath
import os.path

STATUS_STAY = 0
STATUS_WALK = 1
STATUS_RUN = 2
STATE_MOTION = {STATUS_STAY:"Sapphiart@idle", STATUS_WALK:"Sapphiart@walk", STATUS_RUN:"Sapphiart@running"}

TRANSIT_TIME = 0.2
MOVING_DISTANCE = 0.5


class Character():
    def __init__( self):
        self.currentState = STATUS_STAY
        self.nextState = STATUS_STAY
        self.figure = pyxie.figure('Sapphiart/Sapphiart')
        self.figure.connectAnimator(pyxie.ANIMETION_SLOT_A0, STATE_MOTION[self.currentState])
        self.currentDir= vmath.vec3(0,0,1)
        self.gorlDir= vmath.vec3(0,0,1)
        self.currentPosition = vmath.vec3(0,0,0)
        self.transitTime = 0.0

    def step(self, moveVector):

        l = vmath.length(moveVector)
        if l > 20.0:
            self.gorlDir = vmath.normalize(moveVector)
            self.__changeStatus(STATUS_RUN)
        elif l > 5.0:
            self.gorlDir = vmath.normalize(moveVector)
            self.__changeStatus(STATUS_WALK)
        else:
            self.__changeStatus(STATUS_STAY)

        r = vmath.dot(self.currentDir, self.gorlDir)
        if r < 0.99:
            n = vmath.cross(self.currentDir, self.gorlDir)
            ROT = vmath.mat_rotationY((1.0-r)*n.y*0.5, 3)
            self.currentDir = vmath.normalize(ROT * self.currentDir)

        if self.currentState == STATUS_RUN:
            self.currentPosition += self.currentDir * 0.06
        elif self.currentState == STATUS_WALK:
            self.currentPosition += self.currentDir * 0.02

        self.__transitMotion()

        self.figure.rotation = vmath.normalize(vmath.quat_rotation((0, 0, 1), self.currentDir))
        self.figure.position = self.currentPosition
        self.figure.step()



    def __changeStatus(self, status):
        if status != self.currentState and status != self.nextState:
            self.nextState = status
            self.figure.connectAnimator(pyxie.ANIMETION_SLOT_A1, STATE_MOTION[status])
            self.transitTime = 0.0

    def __transitMotion(self):
        if self.currentState != self.nextState:

            if self.transitTime >= TRANSIT_TIME:
                self.currentState = self.nextState
                self.figure.connectAnimator(pyxie.ANIMETION_SLOT_A0, STATE_MOTION[self.currentState])
                self.figure.connectAnimator(pyxie.ANIMETION_SLOT_A1)
                return

            self.transitTime += pyxie.getElapsedTime()
            if self.transitTime > TRANSIT_TIME:
                self.transitTime = TRANSIT_TIME
            self.figure.setBlendingWeight(pyxie.ANIMETION_PART_A, self.transitTime / TRANSIT_TIME)


