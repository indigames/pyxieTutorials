import igeBullet
from utils import Utils

class Vehicle():
    def __init__( self):
        self.vehicleSteering = -0.4
        self.engineForce = 10.0
        self.breakingForce = 0.0

    def setup(self, world):
        world.clear()
        efig = Utils().GetFigure()
        efig.clearMesh()

        shape = igeBullet.shape(igeBullet.BOX_SHAPE_PROXYTYPE, halfExtents=(10,1,10))
        self.ground = igeBullet.rigidBody(shape,0,(0,0,0),(0,0,0,1))
        world.add(self.ground)
        Utils().AddShapeMesh(shape)

        compound = igeBullet.shape(igeBullet.COMPOUND_SHAPE_PROXYTYPE)
        chassisShape = igeBullet.shape(igeBullet.BOX_SHAPE_PROXYTYPE, halfExtents=(1.0, 0.5, 2.0))
        compound.addChildShape(chassisShape,(0, 1, 0),(0,0,0,1))
        suppShape = igeBullet.shape(igeBullet.BOX_SHAPE_PROXYTYPE, halfExtents=(0.5, 0.1, 0.5))
        compound.addChildShape(suppShape, (0, 1.0, 2.5),(0,0,0,1))
        self.carChassis = igeBullet.rigidBody(compound, 10, (7, 1, 0), (0, 0, 0, 1))
        world.add(self.carChassis)
        Utils().AddShapeMesh(compound)

        wheelRadius = 0.5
        wheelWidth = 0.4
        wheelShape = igeBullet.shape(igeBullet.CYLINDER_SHAPE_PROXYTYPE, halfExtents=(wheelWidth, wheelRadius, wheelRadius), axis=0)
        Utils().AddShapeMesh(wheelShape)
        Utils().AddShapeMesh(wheelShape)
        Utils().AddShapeMesh(wheelShape)
        Utils().AddShapeMesh(wheelShape)
        self.vehicle = igeBullet.vehicle(world, self.carChassis)
        world.add(self.vehicle)

        connectionHeight = 1.2
        CUBE_HALF_EXTENTS = 1.0
        suspensionRestLength = 0.6
        wheelDirectionCS0 = (0, -1, 0)
        wheelAxleCS = (-1, 0, 0)

        isFrontWheel = True
        connectionPointCS0 = (CUBE_HALF_EXTENTS - (0.3 * wheelWidth), connectionHeight, 2 * CUBE_HALF_EXTENTS - wheelRadius)
        self.vehicle.addWheel(connectionPointCS0, wheelDirectionCS0, wheelAxleCS, suspensionRestLength, wheelRadius, isFrontWheel);
        connectionPointCS0 = (-CUBE_HALF_EXTENTS + (0.3 * wheelWidth), connectionHeight,2 * CUBE_HALF_EXTENTS - wheelRadius);
        self.vehicle.addWheel(connectionPointCS0, wheelDirectionCS0, wheelAxleCS, suspensionRestLength, wheelRadius, isFrontWheel);
        isFrontWheel = False
        connectionPointCS0 = (-CUBE_HALF_EXTENTS + (0.3 * wheelWidth), connectionHeight,-2 * CUBE_HALF_EXTENTS + wheelRadius);
        self.vehicle.addWheel(connectionPointCS0, wheelDirectionCS0, wheelAxleCS, suspensionRestLength, wheelRadius, isFrontWheel);
        connectionPointCS0 = (CUBE_HALF_EXTENTS - (0.3 * wheelWidth), connectionHeight,-2 * CUBE_HALF_EXTENTS + wheelRadius);
        self.vehicle.addWheel(connectionPointCS0, wheelDirectionCS0, wheelAxleCS, suspensionRestLength, wheelRadius, isFrontWheel);

        efig.mergeMesh()

        """
        for (int i = 0; i < m_vehicle->getNumWheels(); i++)
        {
            btWheelInfo & wheel = m_vehicle->getWheelInfo(i);
            wheel.m_suspensionStiffness = suspensionStiffness;
            wheel.m_wheelsDampingRelaxation = suspensionDamping;
            wheel.m_wheelsDampingCompression = suspensionCompression;
            wheel.m_frictionSlip = wheelFriction;
            wheel.m_rollInfluence = rollInfluence;
        }
        """

    def update(self):
        efig = Utils().GetFigure()
        efig.setJoint(1, position=self.carChassis.position, rotation=self.carChassis.rotation)

        for i in range(4):
            efig.setJoint(i+2, position=self.vehicle.getWheelPosition(i), rotation=self.vehicle.getWheelRotation(i))

        wheelIndex = 0
        self.vehicle.setSteeringValue(self.vehicleSteering, wheelIndex)
        wheelIndex = 1
        self.vehicle.setSteeringValue(self.vehicleSteering, wheelIndex)
        wheelIndex = 2
        self.vehicle.applyEngineForce(self.engineForce, wheelIndex)
        self.vehicle.setBrake(self.breakingForce, wheelIndex)
        wheelIndex = 3
        self.vehicle.applyEngineForce(self.engineForce, wheelIndex)
        self.vehicle.setBrake(self.breakingForce, wheelIndex)

