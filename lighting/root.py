"""
indi game engine

Lighting

Use directional lamp sample

"""

import igeCore as core
from igeCore import devtool
from igeCore import apputil
from igeCore.apputil import graphicsHelper

import igeVmath as vmath
import os

devtool.convertAssets('.', '.', core.TARGET_PLATFORM_PC,0.1)

core.window(True, 480, 640)

figure = core.figure('sample')

arrow = core.figure('arrow')
arrow.position = (0,0.5,0)

cam = core.camera()
cam.position = (0,1,2)
cam.target = (0,0,0)

env = core.environment()
env.setDirectionalLampColor(0, (0.9, 0.8, 1.0))

showcase = core.showcase("case")
showcase.add(env)
showcase.add(figure)
showcase.add(arrow)

head = 0.0
pitch = 0.0

while True:

    touch = core.singleTouch()
    if touch is not None:
        if touch['is_moved']:
            pitch += touch['delta_x']*0.005
            head += touch['delta_y']*0.005
            moved = True

    rot = vmath.mat_rotationZYX(3, (head, pitch, 0.0))
    arrow.rotation = vmath.quat(rot)
    env.setDirectionalLampDirection(0, rot.getCol(2))   #vec3 direcrtion vector

    cam.shoot(showcase)
    core.swap()
