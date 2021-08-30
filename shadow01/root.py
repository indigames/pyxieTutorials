"""

Shadow mapping sample

"""


import igeCore as core
from igeCore.apputil import graphicsHelper
import igeVmath as vmath


#asset convert
from igeCore import devtool
devtool.convertAssets('.','.', core.TARGET_PLATFORM_MOBILE,0.1)


core.window(True, 640, 480)

core.shaderGenerator().globalShadowBias = 0.001


#ground plane
ground = core.figure('ground')
for i in range(ground.numMaterials):
    shaderGen = ground.getShaderGenerator(i)    #get current shader
    shaderGen.setShadow(False,True,True)        #add shadow function(no make shadow, receive shadow, depth shadow)
    ground.setShaderGenerator(i, shaderGen)     #set new shader

#scene object
box = core.figure('box')
for i in range(box.numMaterials):
    shaderGen = box.getShaderGenerator(i)       #get current shader
    shaderGen.setShadow(True,True,True)         #add shadow function(make shadow, receive shadow, depth shadow)
    box.setShaderGenerator(i, shaderGen)        #set new shader

cam = core.camera()
cam.position = (-100,100,100)
cam.target = (0,0,0)

#create shadow buffer
shadowBuffer = core.texture('Shadow', 1024,1024, format=core.GL_RED, depth=True, float=True)

env = core.environment()

#The direction of the shadow is determined by the 0th directional light
env.setDirectionalLampDirection(0, (5,5,5))    
env.shadowColor = (0.0, 0.0, 0.0)

#Sets the color density of the shadow
env.shadowDensity = 0.5

#Specifies the size of the area where the shadow is created.
#The smaller the area, the higher the shadow resolution.
env.shadowWideness = 500.0

env.ambientColor = (0.2,0.2,0.2)

showcase = core.showcase("case")
showcase.add(ground, 1.0)
showcase.add(box, 1.0)

showcase.add(env)

#The shadow buffer needs to be set to Showcase
showcase.addShadowBuffer(shadowBuffer)

#For viewing the shadow buffer
shadowSprite = graphicsHelper.createSprite(100,100,shadowBuffer)
shadowSprite.position = (-100,0,0)
cam2D = core.camera("cam2D")
cam2D.position = (0,0,100)
cam2D.orthographicProjection = True
showcase2D = core.showcase('case2D')
showcase2D.add(shadowSprite)


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

    #make shadow buffer
    cam.shoot(showcase, shadowBuffer, renderPass=core.PASS_SHADOW)

    cam.shoot(showcase)

    cam2D.shoot(showcase2D,clearColor=False)

    core.swap()
