
"""
shader effect sample
"""

import igeCore as core
from igeCore.apputil import graphicsHelper
import igeVmath as vmath

from igeCore import devtool
devtool.convertAssets('.','.', core.TARGET_PLATFORM_ANDROID,0.1)

core.window(True, 480, 640)

shader = core.shaderGenerator()
shader.setColorTexture(True)            #use color texture
shader.setDistortion(True)              #add distortion effect
shader.setUVScroll(1,True)              #start uv scroll at uv channel 1
shader.setNormalTextureUVSet(1, 1)  #change normal texture uv channel to 1
shader.setProjectionMapping(1, True)    #projection mapping mode at uv channel 1

print(shader)                           #print shader program

shadowSprite = graphicsHelper.createSprite(200,200,"fire",shader=shader)

#set uv scroll speed for uv set 1
shadowSprite.setMaterialParam("mate", "ScrollSpeedSet1", (0.0, -0.08));

#set distortion strength
shadowSprite.setMaterialParam("mate", "DistortionStrength", (0.02,));

#set normal texture for distortion
shadowSprite.setMaterialParamTexture("mate", "NormalSampler", "NormalMap",
                                wrap_s=core.SAMPLERSTATE_WRAP,wrap_t=core.SAMPLERSTATE_WRAP,
                                minfilter=core.SAMPLERSTATE_LINEAR, magfilter=core.SAMPLERSTATE_LINEAR)
cam2D = core.camera("cam2D")
cam2D.position = (0,0,100)
cam2D.orthographicProjection = True

showcase2D = core.showcase('case2D')
showcase2D.add(shadowSprite)

while True:
    core.update()
    cam2D.shoot(showcase2D)
    core.swap()

