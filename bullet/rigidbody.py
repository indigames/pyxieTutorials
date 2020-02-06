import igeBullet
from utils import Utils

class Rigidbody():
    def __init__( self):
        None

    def setup(self, world):
        world.clear()
        efig = Utils().GetFigure()
        efig.clearMesh()

        #shape = igeBullet.shape(igeBullet.STATIC_PLANE_PROXYTYPE, normal=(0,1,0), constant=0)
        shape = igeBullet.shape(igeBullet.BOX_SHAPE_PROXYTYPE, halfExtents=(10,1,10))
        self.body1 = igeBullet.rigidBody(shape,0,(0,0,0),(0,0,0,1))
        world.add(self.body1)
        Utils().AddShapeMesh(shape)

        shape = igeBullet.shape(igeBullet.SPHERE_SHAPE_PROXYTYPE, radius = 1)
        self.body2 = igeBullet.rigidBody(shape,5,(0,15,0),(0,0,0,1))
        world.add(self.body2)
        Utils().AddShapeMesh(shape)

        efig.mergeMesh()

    def update(self):
        efig = Utils().GetFigure()
        efig.setJoint(0, position=self.body1.position, rotation=self.body1.rotation)
        efig.setJoint(1, position=self.body2.position, rotation=self.body2.rotation)
