"""
"""
import igeCore as core
import igeBullet
import os
from utils import Utils
import igeVmath as vmath


from igeCore import devtool
devtool.convertAssets('.','.', core.TARGET_PLATFORM_MOBILE)

utl = Utils()
core.window(True, 480, 640)

world = igeBullet.world(True)

efig =utl.GetFigure()
efig.clearMesh()
shape = igeBullet.shape(igeBullet.BOX_SHAPE_PROXYTYPE, halfExtents=(15,2,15))
body1 = igeBullet.rigidBody(shape,0,(0,0,0),(0,0,0,1))
world.add(body1)
utl.AddShapeMesh(shape)

shape = igeBullet.shape(igeBullet.BOX_SHAPE_PROXYTYPE, halfExtents = (3, 3, 3))
body2 = igeBullet.rigidBody(shape,5,(5,8,0),(0,0,0,1))
world.add(body2)
utl.AddShapeMesh(shape)

sphere = core.figure('box')
poss = sphere.getVertexElements(0,core.ATTRIBUTE_ID_POSITION)
tris = sphere.getTriangles(0)
soft = igeBullet.softBody(world, poss, tris, mass=5.5, springStiffness=50.0)
soft.transform = ((0,30,0),(0,0,0,1))

print(soft.transform)
#soft.collisionGroupBit = 0
#soft.collisionGroupMask = 0


cam = core.camera()
cam.position = (0, 50, 50)
cam.target = (0, 0, 0)

showcase = core.showcase("case")
showcase.add(efig)
showcase.add(sphere)

rotX = 0
rotY = 0

while True:
    core.update()
    world.step()

    touch = core.singleTouch()
    if touch is not None:
        if touch['is_moved']:
            rotX -= touch['delta_x']*0.05
            rotY += touch['delta_y']*0.05
            cam.pan = rotX
            cam.roll = rotY
        if touch['is_tapped']:
            soft.angularVelocity = (0,0,1);


    efig =utl.GetFigure()
    efig.setJoint(0, position=body1.position, rotation=body1.rotation)
    efig.setJoint(1, position=body2.position, rotation=body2.rotation)

    sphere.setVertexElements(0, core.ATTRIBUTE_ID_POSITION, soft.meshPositions())
    sphere.setVertexElements(0, core.ATTRIBUTE_ID_NORMAL, soft.meshNormals())

    #rv = world.contactPairTest(soft, body2)
    #rv = world.contactTest(soft)
    rv = world.rayTestAll((0,10,-10), (0,10,10))
    if rv != None:
        print(rv)

    cam.shoot(showcase)
    core.swap()
