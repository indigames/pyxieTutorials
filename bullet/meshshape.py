import igeBullet
import igeCore
from utils import Utils

class Meshshape():
    def __init__( self):
        None

    def setup(self, world):
        world.clear()
        efig = Utils().GetFigure()
        efig.clearMesh()

        #shape = igeBullet.shape(igeBullet.STATIC_PLANE_PROXYTYPE, normal=(0,1,0), constant=0)
        #shape = igeBullet.shape(igeBullet.BOX_SHAPE_PROXYTYPE, halfExtents=(10,1,10))
        figure = igeCore.figure('ground')
        points = figure.getVertexElements(0,igeCore.ATTRIBUTE_ID_POSITION)
        triangles = figure.getTriangles(0)
        shape = igeBullet.shape(igeBullet.TRIANGLE_MESH_SHAPE_PROXYTYPE, points = points, triangles = triangles)
        self.body1 = igeBullet.rigidBody(shape,0,(0,0,0),(0,0,0,1))
        world.add(self.body1)
        Utils().AddShapeMesh(shape)

        figure = igeCore.figure('shape')
        points = figure.getVertexElements(0,igeCore.ATTRIBUTE_ID_POSITION)
        triangles = figure.getTriangles(0)
        #shape = igeBullet.shape(igeBullet.TRIANGLE_MESH_SHAPE_PROXYTYPE, points = points, triangles = triangles)
        #shape = igeBullet.shape(igeBullet.SPHERE_SHAPE_PROXYTYPE, radius = 1)
        shape = igeBullet.shape(igeBullet.CONVEX_HULL_SHAPE_PROXYTYPE, points = points)
        self.body2 = igeBullet.rigidBody(shape,5,(0,15,0),(0,0,0,1))
        world.add(self.body2)
        Utils().AddShapeMesh(shape)

        efig.mergeMesh()

    def update(self):
        efig = Utils().GetFigure()
        efig.setJoint(0, position=self.body1.position, rotation=self.body1.rotation)
        efig.setJoint(1, position=self.body2.position, rotation=self.body2.rotation)
