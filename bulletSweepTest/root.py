import igeCore as core
import igeBullet
from utils import Utils

def addObject(world, type, mass, position, size=(1,1,1), radius=1, height=3, name='body'):
    if type == igeBullet.BOX_SHAPE_PROXYTYPE:
        shape = igeBullet.shape(type, halfExtents=size)
    elif type == igeBullet.SPHERE_SHAPE_PROXYTYPE:
        shape = igeBullet.shape(type, radius=radius)
    elif type ==igeBullet.CAPSULE_SHAPE_PROXYTYPE:
        shape = igeBullet.shape(type, radius=radius, height=height)
    elif type ==igeBullet.CONE_SHAPE_PROXYTYPE:
        shape = igeBullet.shape(type, radius=radius, height=height)
    elif type ==igeBullet.CYLINDER_SHAPE_PROXYTYPE:
        shape = igeBullet.shape(type, halfExtents=size)

    body = igeBullet.rigidBody(shape, mass, position, (0, 0, 0, 1))
    body.name = name
    world.add(body)
    Utils().AddShapeMesh(shape)
    return body


core.window(True, 480, 640)

case = core.showcase()
case.add(Utils().GetFigure())
camera = core.camera("cam01")
camera.position = (-30, 30, -30)

world = igeBullet.world()
world.gravity = (0,-10,0)

ground = addObject(world, igeBullet.BOX_SHAPE_PROXYTYPE, 0, position=(0,0,0), size=(10,1,10), name='ground')
bodyA = addObject(world, igeBullet.BOX_SHAPE_PROXYTYPE, 1, position=(8,6,8), name='bodyA')
bodyB = addObject(world, igeBullet.BOX_SHAPE_PROXYTYPE, 1, position=(-8,6,-8), name='bodyB')
addObject(world, igeBullet.SPHERE_SHAPE_PROXYTYPE, 1, position=(2,6,0), name='sphere')
addObject(world, igeBullet.CAPSULE_SHAPE_PROXYTYPE, 1, position=(0,6,2), name='capsule')
addObject(world, igeBullet.CONE_SHAPE_PROXYTYPE, 1, position=(-2,6,0), name='cone')
addObject(world, igeBullet.SPHERE_SHAPE_PROXYTYPE, 1, position=(2,9,0), name='sphere')
addObject(world, igeBullet.CAPSULE_SHAPE_PROXYTYPE, 1, position=(0,9,2), name='capsule')
addObject(world, igeBullet.CONE_SHAPE_PROXYTYPE, 1, position=(-2,9,0), name='cone')

bodyA.collisionGroupBit = 4
ground.collisionGroupMask = 7

while True:
    rv = world.convexSweepTest(bodyA.shape, bodyA.transform, bodyB.transform, 0.1)
    print('----------------------')
    for i in rv:
        print(i['collisionObject'].name)

    world.step()
    Utils().Update(world)
    camera.shoot(case)

    core.swap()
