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
devtool.convertAssets('.','.', pyxie.TARGET_PLATFORM_PC)

# open or resize window (This function is valid only on PC,Ignored in smartphone apps)
pyxie.window(True, 480, 640)


char = Character()
cam = TargetCamera()
controller = Controller()
ground = graphicsHelper.createSprite(20.0,20.0,texture ='images/Dirt-2290', normal=(0,1,0))

tex = pyxie.texture("offscreen",256,256, depth=True)
efig = graphicsHelper.createSprite(100, 100, tex)
efig.position = vmath.vec3(-100, 200, 0)

# what you want to draw should be registered in showcase
showcase2D = pyxie.showcase('2dcase')
showcase3D = pyxie.showcase("3dcase")

showcase3D.add(ground)
showcase3D.add(char.figure)

showcase2D.add(efig)
showcase2D.add(controller.frame)
showcase2D.add(controller.button)

cam2D = pyxie.camera('2dcam')
cam2D.orthographicProjection = True
cam2D.position = (0, 0, 100)

loop = True
while loop:
    dv = 0.0
    moveVector = vmath.vec3(0.0, 0.0, 0.0)

    touch = pyxie.singleTouch()
    if touch is not None:
        moveVector = vmath.vec3(touch['cur_x'] - touch['org_x'], 0, -(touch['cur_y'] - touch['org_y']))
        d = vmath.length(moveVector)

    viewMat = cam.getWalkThroughMatrix()
    moveVector = vmath.vec3(viewMat * moveVector)
    char.step(moveVector)
    cam.step(char.figure)
    controller.step()

    cam.camera.shoot(showcase3D, tex)  # render to texture
    cam.camera.shoot(showcase3D)
    cam2D.shoot(showcase2D, clearColor=False)

    pyxie.swap()


