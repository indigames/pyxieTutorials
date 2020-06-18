
"""
"""

import igeCore as core
from igeCore.apputil import graphicsHelper
import igeVmath as vmath

from igeCore import devtool
devtool.convertAssets('.','.', core.TARGET_PLATFORM_ANDROID,0.1)

core.window(True, 800, 320)

#core.autoSaveShader("shaders")
#core.autoReadShader("shaders")


box = core.figure('char0/char0')
box.setMaterialParam(0, "ScrollSpeedSet1", (0.0, -0.08));
box.setMaterialParam(0, "DistortionStrength", (0.02,));
box.setMaterialParamTexture(0, "NormalSampler", "char0/NormalMap",
                            wrap_s=core.SAMPLERSTATE_WRAP,wrap_t=core.SAMPLERSTATE_WRAP,
                            minfilter=core.SAMPLERSTATE_LINEAR, magfilter=core.SAMPLERSTATE_LINEAR)

ground = core.figure('ground/ground')

cam = core.camera()
cam.position = (-100,100,100)
cam.target = (0,0,0)

showcase = core.showcase("case")
showcase.add(ground, 1.0)
showcase.add(box, 1.0)


rotX = 0
rotY = 0

while True:
    core.update()
    box.step()
    touch = core.singleTouch()
    if touch is not None:
        if touch['is_moved']:
            rotX -= touch['delta_x']*0.05
            rotY += touch['delta_y']*0.05
            cam.pan = rotX
            cam.roll = rotY

    cam.shoot(showcase)
    core.swap()
