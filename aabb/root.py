"""
"""

import igeCore as core
from igeCore import devtool
from igeCore import apputil
from igeCore.apputil import graphicsHelper
import igeVmath as vmath
import os
import imgui
from igeCore.apputil.imguirenderer import ImgiIGERenderer
import shapes

devtool.convertAssets('.','.', core.TARGET_PLATFORM_ANDROID,0.1)

core.window(True, 480, 640)

#locale, language = core.getLocaleLanguage()

# imgui.create_context()
# impl = ImgiIGERenderer()


def createEditableFigure():
    shader = core.shaderGenerator()
    shader.setBoneCondition(1, 1)
    shader.setAmbientType(core.AMBIENT_TYPE_AMBIENT)
    shader.setNumDirLamp(1)
    efig = core.editableFigure('figure')
    efig.addMaterial("mate", shader)
    efig.addMesh("mesh", "mate")
    efig.addJoint("joint")
    efig.setMaterialParam("mate", "DiffuseColor", (1.0, 1.0, 1.0, 1.0))
    return efig

figure1 = core.figure('bone')
figure1.setMeshWireframe(0, True)
figure1.position = (-0.5,0,0)
figure2 = core.figure('bone')
figure2.setMeshWireframe(0, True)
figure2.position = (0.5,0,0)

text = graphicsHelper.textFigure("LocalSpace        WorldSpace", "ume-pgc5.ttf", 23, scale=0.005)
text.position = (0, 0.3, 0)

cam = core.camera()
cam.orthographicProjection = True
cam.widthBase = True
cam.orthoWidth = 1.0
cam.position = (0,0,2)
cam.target = (0,0,0)

aabbBox1 = createEditableFigure()
aabbBox1.position = figure1.position
aabbBox2 = createEditableFigure()

showcase = core.showcase("case")
showcase.add(figure1, 1.0)
showcase.add(figure2, 1.0)
showcase.add(aabbBox1, 1.0)
showcase.add(aabbBox2, 1.0)
showcase.add(text, 1.0)

rotX = 0.0
rotY = 0.0

while True:
    min, max = figure1.getAABB(-1, core.LocalSpace)
    poss, noms, uvs, idxs = shapes.makeBoxFromAABB(min, max)
    aabbBox1.setVertexElements("mesh", core.ATTRIBUTE_ID_POSITION, poss)
    aabbBox1.setVertexElements("mesh", core.ATTRIBUTE_ID_NORMAL, noms)
    aabbBox1.setVertexElements("mesh", core.ATTRIBUTE_ID_UV0, uvs)
    aabbBox1.setTriangles("mesh", idxs)
    aabbBox1.setMeshWireframe(0, True)

    min, max = figure2.getAABB(-1, core.WorldSpace)
    poss, noms, uvs, idxs = shapes.makeBoxFromAABB(min, max)
    aabbBox2.setVertexElements("mesh", core.ATTRIBUTE_ID_POSITION, poss)
    aabbBox2.setVertexElements("mesh", core.ATTRIBUTE_ID_NORMAL, noms)
    aabbBox2.setVertexElements("mesh", core.ATTRIBUTE_ID_UV0, uvs)
    aabbBox2.setTriangles("mesh", idxs)
    aabbBox2.setMeshWireframe(0, True)


    touch = core.singleTouch()
    if touch is not None:
        rotX += touch['delta_x']*0.05
        rotY += touch['delta_y']*0.05
        aabbBox1.rotation = vmath.quat_rotationZYX((rotY,rotX, 0.0))
        figure1.rotation = vmath.quat_rotationZYX((rotY,rotX, 0.0))
        figure2.rotation = vmath.quat_rotationZYX((rotY,rotX, 0.0))

    figure1.step()
    figure2.step()
    cam.shoot(showcase)

    core.swap()
