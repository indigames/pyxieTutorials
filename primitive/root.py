
"""
"""
import igeVmath as vmath
import igeCore as core
from igeCore.apputil import graphicsHelper

core.window(True, 480, 640)


def createFigure():
    shader = core.shaderGenerator()
    shader.setBoneCondition(1, 1)
    shader.setAmbientType(core.AMBIENT_TYPE_AMBIENT)
    shader.setNumDirLamp(1)
    efig = core.editableFigure('figure')
    efig.addMaterial("mate", shader)
    efig.setMaterialParam("mate", "DiffuseColor", (1.0, 1.0, 1.0, 1.0))
    return efig

def addMesh(efig, jointIndex, poss, noms, uvs, idxs, triangles):
    jointName = "joint{}".format(jointIndex)
    efig.addJoint(jointName)
    efig.addMesh(jointName, "mate")
    efig.setVertexElements(jointName, core.ATTRIBUTE_ID_POSITION, poss)
    efig.setVertexElements(jointName, core.ATTRIBUTE_ID_NORMAL, noms)
    efig.setVertexElements(jointName, core.ATTRIBUTE_ID_UV0, uvs)
    efig.setVertexElements(jointName, core.ATTRIBUTE_ID_BLENDINDICES, idxs)
    efig.setTriangles(jointName, triangles)
    #fig.setMeshWireframe(jointIndex,True)

fig = createFigure()


poss, noms, uvs, idxs, triangles = graphicsHelper.makePlane(5,5,(0,0),(1,1),(0,1,0), 0)
addMesh(fig, 0, poss, noms, uvs, idxs, triangles)

poss, noms, uvs, idxs, triangles = graphicsHelper.makeTorus(0.2,0.4,8,8, (0,1,0), 1)
addMesh(fig, 1, poss, noms, uvs, idxs, triangles)
fig.setJoint(1, position = (1,0.2,0))

poss, noms, uvs, idxs, triangles = graphicsHelper.makeBox(0.4,0.4,0.4, 2)
addMesh(fig, 2, poss, noms, uvs, idxs, triangles)
fig.setJoint(2, position = (-1,0.2,0))

poss, noms, uvs, idxs, triangles = graphicsHelper.makeSphere(0.4,12,12, 3)
addMesh(fig, 3, poss, noms, uvs, idxs, triangles)
fig.setJoint(3, position = (0,0.4,1))

poss, noms, uvs, idxs, triangles = graphicsHelper.makeCylinder(0.3,0.3,1,12,12, (0,1,0), 4)
addMesh(fig, 4, poss, noms, uvs, idxs, triangles)
fig.setJoint(4, position = (0,0.5,-1))

cam = core.camera()
cam.position = (0,0,10)
cam.target = (0,0,0)

env = core.environment()
env.setDirectionalLampColor(0,(0.5,0.5,0.5))
env.setDirectionalLampDirection(0,(0.3,0.5,0.4))

showcase = core.showcase("case")
showcase.add(env)
showcase.add(fig, 1.0)

rotX = -3.14/2
rotY = 0.0
while True:
    core.update()
    touch = core.singleTouch()
    if touch is not None:
        if touch['is_moved']:
            rotX += touch['delta_x']*0.05
            rotY += touch['delta_y']*0.05
    cam.pan = rotX
    cam.roll = rotY

    cam.shoot(showcase)
    core.swap()
