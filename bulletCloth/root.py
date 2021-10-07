"""
indi game engine
Tutorial04

walk through 3d character with animation
"""
import igeCore as core
from igeCore import devtool
from igeCore.apputil import graphicsHelper
import igeVmath as vmath
import os.path
from char import Character
from cam import TargetCamera
from controller import Controller
import igeBullet
from utils import Utils

utl = Utils()

devtool.convertAssets('.','.', core.TARGET_PLATFORM_PC)
core.window(True, 480, 640)

world = igeBullet.world(True)


ground = graphicsHelper.createSprite(20.0,20.0,texture ='images/Dirt-2290', normal=(0,1,0))
ground_shape = igeBullet.shape(igeBullet.STATIC_PLANE_PROXYTYPE, normal=(0,1,0), constant=0)
ground_body = igeBullet.rigidBody(ground_shape,0,(0,0,0),(0,0,0,1))
world.add(ground_body)

efig =utl.GetFigure()
efig.clearMesh()
shape = igeBullet.shape(igeBullet.SPHERE_SHAPE_PROXYTYPE, radius = 1)
body2 = igeBullet.rigidBody(shape,5,(0,10,0),(0,0,0,1))
world.add(body2)
utl.AddShapeMesh(shape)

char = Character(world)
cam = TargetCamera()
controller = Controller()


# sphere = core.figure('sphere')
# sphere.position = (0,10,0)
# poss = sphere.getVertexElements(0,core.ATTRIBUTE_ID_POSITION, space=core.WorldSpace)
# tris = sphere.getTriangles(0)
# soft = igeBullet.softBody(world, poss, tris)
# sphere.position = (0,0,0)




showcase2D = core.showcase('2dcase')
showcase3D = core.showcase("3dcase")

showcase3D.add(ground)
showcase3D.add(char.figure)
showcase3D.add(efig)

showcase2D.add(controller.frame)
showcase2D.add(controller.button)

cam2D = core.camera('2dcam')
cam2D.orthographicProjection = True
cam2D.position = (0, 0, 100)


loop = True
while loop:
    core.update()
    world.step()

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

    efig =utl.GetFigure()
    efig.setJoint(0, position=body2.position, rotation=body2.rotation)


    cam.camera.shoot(showcase3D)
    cam2D.shoot(showcase2D, clearColor=False)

    core.swap()
