import igeBullet
import igeVmath as vmath
from utils import Utils

class ConeTwist():
    def __init__( self):
        None

    def setup(self, world):
        world.clear()
        efig = Utils().GetFigure()
        efig.clearMesh()

        shape = igeBullet.shape(igeBullet.CAPSULE_SHAPE_PROXYTYPE, 1, 4)

        self.body1 = igeBullet.rigidBody(shape,0,(-3,5,0),vmath.quat(vmath.mat_rotationZYX(3, 0, 0, 3.14/2)))
        world.add(self.body1)
        Utils().AddShapeMesh(shape)

        self.body2 = igeBullet.rigidBody(shape,1,(3,5,0),vmath.quat(vmath.mat_rotationZYX(3, 0, 0, 3.14/2)))
        world.add(self.body2)
        Utils().AddShapeMesh(shape)

        rotA = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, 3.14/2))
        posA = vmath.vec3(0, -3.2, 0)
        rotB = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, 3.14/2))
        posB = vmath.vec3(0,  3.2, 0)
        joint = igeBullet.constraint(igeBullet.CONETWIST_CONSTRAINT_TYPE, self.body1, self.body2,
                                     frameA=(posA, rotA), frameB=(posB, rotB))
        world.add(joint)

        efig.mergeMesh()

    def update(self):
        efig = Utils().GetFigure()
        efig.setJoint(0, position=self.body1.position, rotation=self.body1.rotation)
        efig.setJoint(1, position=self.body2.position, rotation=self.body2.rotation)
