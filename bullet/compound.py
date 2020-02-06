import igeVmath as vmath
import igeBullet
from utils import Utils

class Compound():
    def __init__( self):
        None

    def setup(self, world):
        world.clear()
        efig = Utils().GetFigure()
        efig.clearMesh()

        shape = igeBullet.shape(igeBullet.BOX_SHAPE_PROXYTYPE, halfExtents=(10,1,10))
        self.ground = igeBullet.rigidBody(shape,0,(0,0,0),(0,0,0,1))
        world.add(self.ground)
        Utils().AddShapeMesh(shape)

        compound = igeBullet.shape(igeBullet.COMPOUND_SHAPE_PROXYTYPE)
        box = igeBullet.shape(igeBullet.BOX_SHAPE_PROXYTYPE, halfExtents=(0.5,0.5,0.5))
        compound.addChildShape(box, (0,0,0), (0,0,0,1))
        compound.addChildShape(box, (0,-1,0), (0,0,0,1))
        compound.addChildShape(box, (0,0,1), (0,0,0,1))
        self.body1 = igeBullet.rigidBody(compound,1,(0,20,0),vmath.quat(vmath.mat_rotationZYX(3, 0.4, 0, 0)))
        world.add(self.body1)
        Utils().AddShapeMesh(compound)

        efig.mergeMesh()

    def update(self):
        efig = Utils().GetFigure()
        efig.setJoint(1, position=self.body1.position, rotation=self.body1.rotation)
