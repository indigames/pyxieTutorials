"""
pyxie game engine
Tutorial04

walk through 3d character with animation
"""
import pyxie
from pyxie import devtool
from pyxie.apputil import graphicsHelper
import pyvmath as vmath
import os.path
from char import Character
from cam import TargetCamera
from controller import Controller

# convert all assets to the format suitable for the platform
# devtool module can not be used in the app
# this process should be completed in advance, not at runtime
if not os.path.exists('Sapphiart/Sapphiart.pyxf'):
    devtool.convertAssets('.','.', pyxie.TARGET_PLATFORM_PC)

# open or resize window (This function is valid only on PC,Ignored in smartphone apps)
pyxie.window(True, 480, 640)

char = Character()
cam = TargetCamera()
controller = Controller()

ground = graphicsHelper.createSprite(20.0,20.0,texture ='images/Dirt-2290', normal=(0,1,0))

# what you want to draw should be registered in showcase
showcase = pyxie.showcase("case01")
showcase.add(ground)
showcase.add(char.figure)
loop = True
while loop:

    d=0.0
    moveVector = vmath.vec3(0,0,0)

    touch = pyxie.singleTouch()
    if touch is not None:
        moveVector = vmath.vec3(touch['cur_x'] - touch['org_x'], 0, -(touch['cur_y'] - touch['org_y']))
        d = vmath.length(moveVector)

    viewMat = cam.getWalkThroughMatrix()
    moveVector = vmath.vec3(viewMat * moveVector)
    char.step(moveVector)
    cam.step(char.figure)

    cam.camera.shoot(showcase)

    controller.step()

    pyxie.swap()

