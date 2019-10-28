"""
"""
import pyxie
import pickle
import pybullet as p
import os

castle = 'Castle_200'


# pre process
if not os.path.exists(castle + '.pickle'):
    import deploy
    deploy.convertVoxelModel(castle, '.', '.', pyxie.TARGET_PLATFORM_PC)



pyxie.window(True, 480, 640)

#p.connect(p.GUI)
p.connect(p.DIRECT)
p.setGravity(0, 0, -10)

boxinfo = []
with open(castle + '.pickle', 'rb') as f:
    boxinfo = pickle.load(f)

plane = p.createCollisionShape(p.GEOM_PLANE)
p.createMultiBody(baseMass=0, baseCollisionShapeIndex=plane, basePosition=[0, 0, -1])
shape = p.createCollisionShape(p.GEOM_BOX,
                               halfExtents=[boxinfo[0][3][0] * 0.98, boxinfo[0][3][1] * 0.98, boxinfo[0][3][2] * 0.98])
bodies = []
for data in boxinfo:
    body = p.createMultiBody(baseMass=1, baseCollisionShapeIndex=shape, basePosition=data[0])
    bodies.append(body)

figure = pyxie.figure(castle)
cam = pyxie.camera()
cam.position = (0, -3, 3)
cam.target = (0, 0, 0)

#env = pyxie.environment()
#env.setDirectionalLampDirection(0, cam.position - cam.target)


showcase = pyxie.showcase("case")
showcase.add(figure)

#showcase.add(env)

while True:
    p.stepSimulation()

    index = 1
    for bd in bodies:
        pos, rot = p.getBasePositionAndOrientation(bd)
        figure.setJoint(index, position=pos, rotation=rot)
        index += 1

    # cam.pan += 0.01
    cam.shoot(showcase)
    pyxie.swap()

