import igeVmath as vmath
import igeBullet
from utils import Utils


class Ragdoll():
    def __init__( self):
        None

    def setup(self, world):
        world.clear()
        efig = Utils().GetFigure()
        efig.clearMesh()

        #shape = igeBullet.shape(igeBullet.STATIC_PLANE_PROXYTYPE, normal=(0,1,0), constant=0)
        shape = igeBullet.shape(igeBullet.BOX_SHAPE_PROXYTYPE, halfExtents=(10,1,10))
        body = igeBullet.rigidBody(shape,0,(0,0,0),(0,0,0,1))
        world.add(body)
        Utils().AddShapeMesh(shape)

        scale = 5.0
        offset = vmath.vec3(0, 5, 0)

        M_PI = 3.14159265358979323846
        M_PI_2 = 1.57079632679489661923
        M_PI_4 = 0.785398163397448309616

        BODYPART_PELVIS = 0
        BODYPART_SPINE = 1
        BODYPART_HEAD = 2
        BODYPART_LEFT_UPPER_LEG = 3
        BODYPART_LEFT_LOWER_LEG = 4
        BODYPART_RIGHT_UPPER_LEG = 5
        BODYPART_RIGHT_LOWER_LEG = 6
        BODYPART_LEFT_UPPER_ARM = 7
        BODYPART_LEFT_LOWER_ARM = 8
        BODYPART_RIGHT_UPPER_ARM = 9
        BODYPART_RIGHT_LOWER_ARM = 10
        self.BODYPART_COUNT = 11
        JOINT_PELVIS_SPINE = 0
        JOINT_SPINE_HEAD = 1
        JOINT_LEFT_HIP = 2
        JOINT_LEFT_KNEE = 3
        JOINT_RIGHT_HIP = 4
        JOINT_RIGHT_KNEE = 5
        JOINT_LEFT_SHOULDER = 6
        JOINT_LEFT_ELBOW = 7
        JOINT_RIGHT_SHOULDER = 8
        JOINT_RIGHT_ELBOW = 9
        JOINT_COUNT = 10

        m_shapes = [0] * self.BODYPART_COUNT
        m_shapes[BODYPART_PELVIS] = igeBullet.shape(igeBullet.CAPSULE_SHAPE_PROXYTYPE, 0.15 * scale, 0.20 * scale)
        m_shapes[BODYPART_SPINE] = igeBullet.shape(igeBullet.CAPSULE_SHAPE_PROXYTYPE, 0.15 * scale, 0.28 * scale)
        m_shapes[BODYPART_HEAD] = igeBullet.shape(igeBullet.CAPSULE_SHAPE_PROXYTYPE, 0.10 * scale, 0.05 * scale)
        m_shapes[BODYPART_LEFT_UPPER_LEG] = igeBullet.shape(igeBullet.CAPSULE_SHAPE_PROXYTYPE, 0.07 * scale, 0.45 * scale)
        m_shapes[BODYPART_LEFT_LOWER_LEG] = igeBullet.shape(igeBullet.CAPSULE_SHAPE_PROXYTYPE, 0.05 * scale, 0.37 * scale)
        m_shapes[BODYPART_RIGHT_UPPER_LEG] = igeBullet.shape(igeBullet.CAPSULE_SHAPE_PROXYTYPE, 0.07 * scale, 0.45 * scale)
        m_shapes[BODYPART_RIGHT_LOWER_LEG] = igeBullet.shape(igeBullet.CAPSULE_SHAPE_PROXYTYPE, 0.05 * scale, 0.37 * scale)
        m_shapes[BODYPART_LEFT_UPPER_ARM] = igeBullet.shape(igeBullet.CAPSULE_SHAPE_PROXYTYPE, 0.05 * scale, 0.33 * scale)
        m_shapes[BODYPART_LEFT_LOWER_ARM] = igeBullet.shape(igeBullet.CAPSULE_SHAPE_PROXYTYPE, 0.04 * scale, 0.25 * scale)
        m_shapes[BODYPART_RIGHT_UPPER_ARM] = igeBullet.shape(igeBullet.CAPSULE_SHAPE_PROXYTYPE, 0.05 * scale, 0.33 * scale)
        m_shapes[BODYPART_RIGHT_LOWER_ARM] = igeBullet.shape(igeBullet.CAPSULE_SHAPE_PROXYTYPE, 0.04 * scale, 0.25 * scale)

        for i in range(self.BODYPART_COUNT):
            Utils().AddShapeMesh(m_shapes[i])

        self.m_bodies = [0] * self.BODYPART_COUNT
        pos = vmath.vec3(0, 1, 0) * scale + offset
        rot = vmath.quat()
        self.m_bodies[BODYPART_PELVIS] = igeBullet.rigidBody(m_shapes[BODYPART_PELVIS], 1, pos, rot)
        world.add(self.m_bodies[BODYPART_PELVIS])

        pos = vmath.vec3(0, 1.2, 0) * scale + offset
        self.m_bodies[BODYPART_SPINE] = igeBullet.rigidBody(m_shapes[BODYPART_SPINE], 1, pos, rot)
        world.add(self.m_bodies[BODYPART_SPINE])

        pos = vmath.vec3(0, 1.6, 0) * scale + offset
        self.m_bodies[BODYPART_HEAD] = igeBullet.rigidBody(m_shapes[BODYPART_HEAD], 1, pos, rot)
        world.add(self.m_bodies[BODYPART_HEAD])

        pos = vmath.vec3(-0.18, 0.65, 0) * scale + offset
        self.m_bodies[BODYPART_LEFT_UPPER_LEG] = igeBullet.rigidBody(m_shapes[BODYPART_LEFT_UPPER_LEG], 1, pos, rot)
        world.add(self.m_bodies[BODYPART_LEFT_UPPER_LEG])

        pos = vmath.vec3(-0.18, 0.2, 0) * scale + offset
        self.m_bodies[BODYPART_LEFT_LOWER_LEG] = igeBullet.rigidBody(m_shapes[BODYPART_LEFT_LOWER_LEG], 1, pos, rot)
        world.add(self.m_bodies[BODYPART_LEFT_LOWER_LEG])

        pos = vmath.vec3(0.18, 0.65, 0) * scale + offset
        self.m_bodies[BODYPART_RIGHT_UPPER_LEG] = igeBullet.rigidBody(m_shapes[BODYPART_RIGHT_UPPER_LEG], 1, pos, rot)
        world.add(self.m_bodies[BODYPART_RIGHT_UPPER_LEG])

        pos = vmath.vec3(0.18, 0.2, 0) * scale + offset
        self.m_bodies[BODYPART_RIGHT_LOWER_LEG] = igeBullet.rigidBody(m_shapes[BODYPART_RIGHT_LOWER_LEG], 1, pos, rot)
        world.add(self.m_bodies[BODYPART_RIGHT_LOWER_LEG])

        pos = vmath.vec3(-0.35, 1.45, 0) * scale + offset
        rot = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, M_PI_2))
        self.m_bodies[BODYPART_LEFT_UPPER_ARM] = igeBullet.rigidBody(m_shapes[BODYPART_LEFT_UPPER_ARM], 1, pos, rot)
        world.add(self.m_bodies[BODYPART_LEFT_UPPER_ARM])

        pos = vmath.vec3(-0.7, 1.45, 0) * scale + offset
        rot = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, M_PI_2))
        self.m_bodies[BODYPART_LEFT_LOWER_ARM] = igeBullet.rigidBody(m_shapes[BODYPART_LEFT_LOWER_ARM], 1, pos, rot)
        world.add(self.m_bodies[BODYPART_LEFT_LOWER_ARM])

        pos = vmath.vec3(0.35, 1.45, 0) * scale + offset
        rot = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, -M_PI_2))
        self.m_bodies[BODYPART_RIGHT_UPPER_ARM] = igeBullet.rigidBody(m_shapes[BODYPART_RIGHT_UPPER_ARM], 1, pos, rot)
        world.add(self.m_bodies[BODYPART_RIGHT_UPPER_ARM])

        pos = vmath.vec3(0.7, 1.45, 0) * scale + offset
        rot = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, -M_PI_2))
        self.m_bodies[BODYPART_RIGHT_LOWER_ARM] = igeBullet.rigidBody(m_shapes[BODYPART_RIGHT_LOWER_ARM], 1, pos, rot)
        world.add(self.m_bodies[BODYPART_RIGHT_LOWER_ARM])

        for i in range(self.BODYPART_COUNT):
            self.m_bodies[i].linearDamping = 0.05
            self.m_bodies[i].angularDamping = 0.85
            self.m_bodies[i].deactivationTime = 0.8
            self.m_bodies[i].linearSleepingThreshold = 1.6
            self.m_bodies[i].angularSleepingThreshold = 2.5

        m_joints = [0] * JOINT_COUNT
        rotA = vmath.quat(vmath.mat_rotationZYX(3, 0, M_PI_2, 0))
        posA = vmath.vec3(0, 0.15, 0) * scale
        rotB = vmath.quat(vmath.mat_rotationZYX(3, 0, M_PI_2, 0))
        posB = vmath.vec3(0, -0.15, 0) * scale
        m_joints[JOINT_PELVIS_SPINE] = igeBullet.constraint(igeBullet.HINGE_CONSTRAINT_TYPE, self.m_bodies[BODYPART_PELVIS],
                                                            self.m_bodies[BODYPART_SPINE], frameA=(posA, rotA),
                                                            frameB=(posB, rotB))
        m_joints[JOINT_PELVIS_SPINE].setLimit(-M_PI_4, M_PI_2)
        world.add(m_joints[JOINT_PELVIS_SPINE], True)

        rotA = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, M_PI_2))
        posA = vmath.vec3(0, 0.3, 0) * scale
        rotB = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, M_PI_2))
        posB = vmath.vec3(0, -0.14, 0) * scale
        m_joints[JOINT_SPINE_HEAD] = igeBullet.constraint(igeBullet.CONETWIST_CONSTRAINT_TYPE, self.m_bodies[BODYPART_SPINE],
                                                          self.m_bodies[BODYPART_HEAD], frameA=(posA, rotA), frameB=(posB, rotB))
        m_joints[JOINT_SPINE_HEAD].setLimit(M_PI_4, M_PI_4, M_PI_2)
        world.add(m_joints[JOINT_SPINE_HEAD], True)

        rotA = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, -M_PI_4 * 5))
        posA = vmath.vec3(-0.18, -0.10, 0) * scale
        rotB = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, -M_PI_4 * 5))
        posB = vmath.vec3(0, 0.225, 0) * scale
        m_joints[JOINT_LEFT_HIP] = igeBullet.constraint(igeBullet.CONETWIST_CONSTRAINT_TYPE, self.m_bodies[BODYPART_PELVIS],
                                                        self.m_bodies[BODYPART_LEFT_UPPER_LEG], frameA=(posA, rotA),
                                                        frameB=(posB, rotB))
        m_joints[JOINT_LEFT_HIP].setLimit(M_PI_4, M_PI_4, 0)
        world.add(m_joints[JOINT_LEFT_HIP], True)

        rotA = vmath.quat(vmath.mat_rotationZYX(3, 0, M_PI_2, 0))
        posA = vmath.vec3(0, -0.225, 0) * scale
        rotB = vmath.quat(vmath.mat_rotationZYX(3, 0, M_PI_2, 0))
        posB = vmath.vec3(0, 0.185, 0) * scale
        m_joints[JOINT_LEFT_KNEE] = igeBullet.constraint(igeBullet.HINGE_CONSTRAINT_TYPE, self.m_bodies[BODYPART_LEFT_UPPER_LEG],
                                                         self.m_bodies[BODYPART_LEFT_LOWER_LEG], frameA=(posA, rotA),
                                                         frameB=(posB, rotB))
        m_joints[JOINT_LEFT_KNEE].setLimit(0, M_PI_2)
        world.add(m_joints[JOINT_LEFT_KNEE], True)

        rotA = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, M_PI_4))
        posA = vmath.vec3(0.18, -0.10, 0) * scale
        rotB = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, M_PI_4))
        posB = vmath.vec3(0, 0.225, 0) * scale
        m_joints[JOINT_RIGHT_HIP] = igeBullet.constraint(igeBullet.CONETWIST_CONSTRAINT_TYPE, self.m_bodies[BODYPART_PELVIS],
                                                         self.m_bodies[BODYPART_RIGHT_UPPER_LEG], frameA=(posA, rotA),
                                                         frameB=(posB, rotB))
        m_joints[JOINT_RIGHT_HIP].setLimit(M_PI_4, M_PI_4, 0)
        world.add(m_joints[JOINT_RIGHT_HIP], True)

        rotA = vmath.quat(vmath.mat_rotationZYX(3, 0, M_PI_2, 0))
        posA = vmath.vec3(0, -0.225, 0) * scale
        rotB = vmath.quat(vmath.mat_rotationZYX(3, 0, M_PI_2, 0))
        posB = vmath.vec3(0., 0.185, 0) * scale
        m_joints[JOINT_RIGHT_KNEE] = igeBullet.constraint(igeBullet.HINGE_CONSTRAINT_TYPE,
                                                          self.m_bodies[BODYPART_RIGHT_UPPER_LEG],
                                                          self.m_bodies[BODYPART_RIGHT_LOWER_LEG], frameA=(posA, rotA),
                                                          frameB=(posB, rotB))
        m_joints[JOINT_RIGHT_KNEE].setLimit(0, M_PI_2)
        world.add(m_joints[JOINT_RIGHT_KNEE], True)

        rotA = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, M_PI))
        posA = vmath.vec3(-0.2, 0.15, 0) * scale
        rotB = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, M_PI))
        posB = vmath.vec3(0, -0.18, 0) * scale
        m_joints[JOINT_LEFT_SHOULDER] = igeBullet.constraint(igeBullet.CONETWIST_CONSTRAINT_TYPE, self.m_bodies[BODYPART_SPINE],
                                                             self.m_bodies[BODYPART_LEFT_UPPER_ARM], frameA=(posA, rotA),
                                                             frameB=(posB, rotB))
        m_joints[JOINT_LEFT_SHOULDER].setLimit(M_PI_2, M_PI_2, 0)
        world.add(m_joints[JOINT_LEFT_SHOULDER], True)

        rotA = vmath.quat(vmath.mat_rotationZYX(3, 0, M_PI_2, 0))
        posA = vmath.vec3(0, 0.18, 0) * scale
        rotB = vmath.quat(vmath.mat_rotationZYX(3, 0, M_PI_2, 0))
        posB = vmath.vec3(0, -0.14, 0) * scale
        m_joints[JOINT_LEFT_ELBOW] = igeBullet.constraint(igeBullet.HINGE_CONSTRAINT_TYPE,
                                                          self.m_bodies[BODYPART_LEFT_UPPER_ARM],
                                                          self.m_bodies[BODYPART_LEFT_LOWER_ARM], frameA=(posA, rotA),
                                                          frameB=(posB, rotB))
        m_joints[JOINT_LEFT_ELBOW].setLimit(-M_PI_2, 0)
        world.add(m_joints[JOINT_LEFT_ELBOW], True)

        rotA = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, 0))
        posA = vmath.vec3(0.2, 0.15, 0) * scale
        rotB = vmath.quat(vmath.mat_rotationZYX(3, 0, 0, M_PI_2))
        posB = vmath.vec3(0, -0.18, 0) * scale
        m_joints[JOINT_RIGHT_SHOULDER] = igeBullet.constraint(igeBullet.CONETWIST_CONSTRAINT_TYPE, self.m_bodies[BODYPART_SPINE],
                                                              self.m_bodies[BODYPART_RIGHT_UPPER_ARM], frameA=(posA, rotA),
                                                              frameB=(posB, rotB))
        m_joints[JOINT_RIGHT_SHOULDER].setLimit(M_PI_2, M_PI_2, 0)
        world.add(m_joints[JOINT_RIGHT_SHOULDER], True)

        rotA = vmath.quat(vmath.mat_rotationZYX(3, 0, M_PI_2, 0))
        posA = vmath.vec3(0, 0.18, 0) * scale
        rotB = vmath.quat(vmath.mat_rotationZYX(3, 0, M_PI_2, 0))
        posB = vmath.vec3(0, -0.14, 0) * scale
        m_joints[JOINT_RIGHT_ELBOW] = igeBullet.constraint(igeBullet.HINGE_CONSTRAINT_TYPE,
                                                           self.m_bodies[BODYPART_RIGHT_UPPER_ARM],
                                                           self.m_bodies[BODYPART_RIGHT_LOWER_ARM], frameA=(posA, rotA),
                                                           frameB=(posB, rotB))
        m_joints[JOINT_RIGHT_ELBOW].setLimit(-M_PI_2, 0)
        world.add(m_joints[JOINT_RIGHT_ELBOW], True)

        efig.mergeSameMaterialMesh()

    def update(self):
        efig = Utils().GetFigure()
        for i in range(self.BODYPART_COUNT):
            efig.setJoint(i+1, position=self.m_bodies[i].position, rotation=self.m_bodies[i].rotation)
