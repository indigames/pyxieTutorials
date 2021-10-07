"""
indi game engine
buildFigure

Convert fbx file to display
"""
import os.path
import igeCore as core
from igeCore import devtool as tools

core.window(True, 512, 512)

cam = core.camera()
cam.position = (0,100,600)
cam.target = (0,100,0)

convertOption = {"BASE_SCALE":1}

#convert figure 01
fig = core.editableFigure("loader", True)
tools.loadModel("human/female01.fbx", fig, convertOption)
tools.findConvertReplaceTextures(fig, ".", ".", core.TARGET_PLATFORM_MOBILE)
fig.saveFigure("human/female01")

#convert figure 02
fig.clear()
tools.loadModel("human/female02.fbx", fig, convertOption)
tools.findConvertReplaceTextures(fig, ".", ".", core.TARGET_PLATFORM_MOBILE)
fig.saveFigure("human/female02")

#convert animation
fig.clear()
tools.loadModel("human/F_clap.FBX", fig, convertOption)
fig.saveAnimation("human/F_clap")

showcase = core.showcase("case")

fig1 = core.figure("human/female01")
fig2 = core.figure("human/female02")
anm = core.animator("human/F_clap")
fig1.connectAnimator(core.ANIMETION_SLOT_A0, anm)
fig2.connectAnimator(core.ANIMETION_SLOT_A0, anm)

fig1.position = (-50,0,0)
fig2.position = ( 50,0,0)

showcase.add(fig1, 1.0)
showcase.add(fig2, 1.0)

rotX = 0
rotY = 0
while True:
    core.update()
    touch = core.singleTouch()
    if touch is not None:
        if touch['is_moved']:
            rotX -= touch['delta_x']*0.05
            rotY += touch['delta_y']*0.05
            cam.pan = rotX
            cam.roll = rotY

    fig1.step()
    fig2.step()

    cam.shoot(showcase)
    core.swap()
