
"""
"""

import igeCore as core
import igeVmath as vmath
import shapes
import sys
import math

core.window(True, 480, 640)

def IntersectRayAABB(p, d, min, max):
    tmin = 0.0
    tmax = sys.float_info.max
    for i in range(3):
        if math.fabs(d.getElem(i)) < sys.float_info.epsilon:
            if p.getElem(i) < min.getElem(i) or p.getElem(i) > max.getElem(i):
                return False, 0, vmath.vec3()
        else:
            ood = 1.0 / d.getElem(i)
            t1 = (min.getElem(i) - p.getElem(i)) * ood
            t2 = (max.getElem(i) - p.getElem(i)) * ood
            if t1 > t2: t1, t2 = t2, t1
            if t1 > tmin: tmin = t1
            if t2 < tmax: tmax = t2
            if tmin > tmax: return False, 0, vmath.vec3()
    q = p + d * tmin
    return True, tmin, q

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

figure2 = core.figure('bone')
figure2.position = (0, 0, 0)

aabbBox2 = createEditableFigure()
min, max = figure2.getAABB(-1, core.WorldSpace)
poss, noms, uvs, idxs = shapes.makeBoxFromAABB(min, max)
aabbBox2.setVertexElements("mesh", core.ATTRIBUTE_ID_POSITION, poss)
aabbBox2.setVertexElements("mesh", core.ATTRIBUTE_ID_NORMAL, noms)
aabbBox2.setVertexElements("mesh", core.ATTRIBUTE_ID_UV0, uvs)
aabbBox2.setTriangles("mesh", idxs)
aabbBox2.setMeshWireframe(0, True)

cam = core.camera()
#cam.orthographicProjection = True
#cam.widthBase = True
#cam.orthoWidth = 1.0
cam.position = (0,1,3)
cam.target = (0,0,0)

showcase = core.showcase("case")
showcase.add(figure2, 1.0)
showcase.add(aabbBox2, 1.0)

markers = []

rotX = 0.0
rotY = 0.0

while True:
    min, max = figure2.getAABB(-1, core.WorldSpace)
    poss, _, _, _ = shapes.makeBoxFromAABB(min, max)
    aabbBox2.setVertexElements("mesh", core.ATTRIBUTE_ID_POSITION, poss)

    touch = core.singleTouch()
    if touch is not None:
        if touch['is_moved']:
            rotX += touch['delta_x']*0.05
            rotY += touch['delta_y']*0.05
            figure2.rotation = vmath.quat_rotationZYX((rotY,rotX, 0.0))
        elif touch['is_tapped']:
            invProj = vmath.inverse(cam.projectionMatrix)
            invView = cam.viewInverseMatrix
            sw, sh = core.viewSize()
            sx = touch['cur_x'] / (sw / 2)
            sy = touch['cur_y'] / (sh / 2)
            near = vmath.vec4(sx, sy, 0.0, 1.0)
            if cam.orthographicProjection:
                near.z = -1.0
            near = invProj * near
            near = invView * near
            near /= near.w
            far = vmath.vec4(sx, sy, 1.0, 1.0)
            far = invProj * far
            far = invView * far
            far /= far.w
            dir = vmath.normalize(far - near)
            hit, dist, pos = IntersectRayAABB(near, dir, min, max)
            if hit:
                print('hit!')

    figure2.step()
    cam.shoot(showcase)
    core.swap()
