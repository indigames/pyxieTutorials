"""
indi game engine
character with shadow

"""
import igeCore as core
from igeCore import devtool
from igeCore.apputil import graphicsHelper
import igeVmath as vmath
import os.path
from char import Character
from cam import TargetCamera
from controller import Controller

devtool.convertAssets('.','.', core.TARGET_PLATFORM_MOBILE)
core.window(True, 480, 640)

core.shaderGenerator().globalShadowBias = 0.001

#core.autoSaveShader('shaders')

#The character shadow is specified to be set at the time of conversion by figure.conf.
#See Sapphiart/figure.conf
char = Character()

cam = TargetCamera()
controller = Controller()


ground = graphicsHelper.createSprite(20.0,20.0,texture ='images/Dirt-2290', normal=(0,1,0))
#add shadow shader 
for i in range(ground.numMaterials):
    shaderGen = ground.getShaderGenerator(i)
    shaderGen.setShadow(False,True,True)
    ground.setShaderGenerator(i, shaderGen)

#create shadow buffer
shadowBuffer = core.texture('Shadow', 1024,1024, format=core.GL_RED, depth=True, float=True)


efig = graphicsHelper.createSprite(100, 100,shadowBuffer)
efig.position = vmath.vec3(-100, 200, 0)

# what you want to draw should be registered in showcase
showcase2D = core.showcase('2dcase')
showcase3D = core.showcase("3dcase")

showcase3D.add(ground)
showcase3D.add(char.figure)

showcase2D.add(efig)
showcase2D.add(controller.frame)
showcase2D.add(controller.button)

showcase3D.addShadowBuffer(shadowBuffer)

#set shadow environment
env = core.environment()
env.setDirectionalLampDirection(0, (5,5,5))
env.shadowColor = (0.0, 0.0, 0.0)
env.shadowDensity = 0.7
env.shadowWideness = 12.0
env.ambientColor = (0.2,0.2,0.2)

showcase3D.add(env)


cam2D = core.camera('2dcam')
cam2D.orthographicProjection = True
cam2D.position = (0, 0, 100)

loop = True
while loop:
    core.update()
    dv = 0.0
    moveVector = vmath.vec3(0.0, 0.0, 0.0)

    touch = core.singleTouch()
    if touch is not None:
        moveVector = vmath.vec3(touch['cur_x'] - touch['org_x'], 0, -(touch['cur_y'] - touch['org_y']))
        d = vmath.length(moveVector)

    viewMat = cam.getWalkThroughMatrix()
    moveVector = vmath.vec3(viewMat * moveVector)
    char.step(moveVector)
    cam.step(char.figure)
    controller.step()

    cam.camera.shoot(showcase3D, shadowBuffer, renderPass=core.PASS_SHADOW)
    cam.camera.shoot(showcase3D)
    cam2D.shoot(showcase2D, clearColor=False)

    core.swap()
