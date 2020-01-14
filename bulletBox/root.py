"""
"""
import igeCore as core
import igeBullet as b
import pickle
import os

castle = 'Castle_200'

# pre process
if not os.path.exists(castle + '.pickle'):
    import deploy
    deploy.convertVoxelModel(castle, '.', '.', core.TARGET_PLATFORM_PC, 10)

core.window(True, 480, 640)

boxinfo = []
with open(castle + '.pickle', 'rb') as f:
    boxinfo = pickle.load(f)

world = b.world()

planeShape = b.shape(b.STATIC_PLANE_PROXYTYPE, normal=(0,1,0), constant=-5)
plane = b.rigidBody(planeShape, 0, (0,0,0), (0,0,0,1))
world.add(plane)

boxShape = b.shape(b.BOX_SHAPE_PROXYTYPE, halfExtents=(boxinfo[0][3][0] * 0.98, boxinfo[0][3][1] * 0.98, boxinfo[0][3][2] * 0.98))

bodies = []
for data in boxinfo:
    body = b.rigidBody(boxShape, 1, data[0], data[1])
    world.add(body)
    bodies.append(body)

figure = core.figure(castle)
cam = core.camera()
cam.position = (0, 30, 30)
cam.target = (0, 0, 0)

showcase = core.showcase("case")
showcase.add(figure)

while True:
    world.step()

    index = 1
    for bd in bodies:
        figure.setJoint(index, position=bd.position, rotation=bd.rotation)
        index += 1

    cam.shoot(showcase)
    core.swap()
