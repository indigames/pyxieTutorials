
from igeCore.apputil import graphicsHelper
import igeVmath as vmath
import igeCore as core
import Box2D

import Defines as DEF


class QueryCallback(Box2D.b2QueryCallback):
    def __init__(self, p):
        super(QueryCallback, self).__init__()
        self.point = p
        self.fixture = None

    def ReportFixture(self, fixture):
        body = fixture.body
        if body.type == Box2D.b2_dynamicBody:
            inside = fixture.TestPoint(self.point)
            if inside:
                self.fixture = fixture
                return False
        return True


class Bowl:
    def __init__(self, world, showcase, cam, pos):
        self.mouseJoint = None
        self.mouseWorld = Box2D.b2Vec2(0.0, 0.0)
        self.mouseTracing = False
        self.mouseTracingPosition = Box2D.b2Vec2(0.0, 0.0)
        self.mouseTracingVelocity = Box2D.b2Vec2(0.0, 0.0)

        self.cam = cam
        self.world = world
        self.ground = world.CreateStaticBody()

        # Create Particle System
        psDef = Box2D.b2ParticleSystemDef()
        psDef.flags = Box2D.b2_waterParticle
        self.particleSystem = world.CreateParticleSystem(psDef)

        # Particle system initialization
        self.particleSystem.SetRadius(DEF.PARTICLE_RADIUS)  # 0.025
        self.particleSystem.SetDensity(DEF.PARTICLE_DENSITY)

        # ground
        shape = Box2D.b2PolygonShape()
        shape.vertices = [
            Box2D.b2Vec2(-40, -10),
            Box2D.b2Vec2(40, -10),
            Box2D.b2Vec2(40, 0),
            Box2D.b2Vec2(-40, 0)]
        self.ground.CreatePolygonFixture(shape=shape, density=0.0)

        # left wall
        shape = Box2D.b2PolygonShape()
        shape.vertices = [
            Box2D.b2Vec2(-40, -0.1),
            Box2D.b2Vec2(-20, -0.1),
            Box2D.b2Vec2(-20, 20),
            Box2D.b2Vec2(-40, 30)]
        self.ground.CreatePolygonFixture(shape=shape, density=0.0)

        # right wall
        shape = Box2D.b2PolygonShape()
        shape.vertices = [
            Box2D.b2Vec2(20, -0.1),
            Box2D.b2Vec2(40, -0.1),
            Box2D.b2Vec2(40, 30),
            Box2D.b2Vec2(20, 20)]
        self.ground.CreatePolygonFixture(shape=shape, density=0.0)

        # add to showcases
        points = []
        for fixture in self.ground.fixtures:
            for point in fixture.shape.vertices:
                points.append(point)
        index = [0, 1, 3, 1, 2, 3, 4, 5, 7, 5, 6, 7, 8, 9, 11, 9, 10, 11]
        self.figure = graphicsHelper.createMesh(points, index)
        showcase.add(self.figure)

        # particle volume
        shape = Box2D.b2PolygonShape()
        shape.SetAsBox(20, 10, Box2D.b2Vec2(0, 10), 0)
        pd = Box2D.b2ParticleGroupDef()
        pd.shape = shape
        pd.color = Box2D.b2ParticleColor(255, 0, 0, 255)
        group = self.particleSystem.CreateParticleGroup(pd)

        # dynamic box 1
        self.body1 = world.CreateDynamicBody()
        shape = Box2D.b2PolygonShape()
        shape.SetAsBox(2, 2, Box2D.b2Vec2(-10, 5), 0)
        self.body1.CreateFixture(Box2D.b2FixtureDef(shape=shape, density=0.1))
        self.particleSystem.DestroyParticlesInShape(
            shape, self.body1.transform)
        points = self.body1.fixtures[0].shape.vertices
        index = (0, 1, 3, 1, 2, 3)
        self.boxF1 = graphicsHelper.createMesh(points, index)
        self.boxF1.position = (
            self.body1.transform.position.x, self.body1.transform.position.y)
        showcase.add(self.boxF1)

        # dynamic box 2
        self.body2 = world.CreateDynamicBody()
        shape.SetAsBox(2, 2, Box2D.b2Vec2(10, 5), 0)
        self.body2.CreateFixture(Box2D.b2FixtureDef(shape=shape, density=0.1))
        self.particleSystem.DestroyParticlesInShape(
            shape, self.body2.transform)
        points = self.body2.fixtures[0].shape.vertices
        index = (0, 1, 3, 1, 2, 3)
        self.boxF2 = graphicsHelper.createMesh(points, index)
        self.boxF2.position = (
            self.body2.transform.position.x, self.body2.transform.position.y)
        showcase.add(self.boxF2)

        # important: make a step to initialize particles position
        world.Step(DEF.TIME_STEP, DEF.VELOCITY_ITERATION,
                   DEF.POSITION_ITERATION, DEF.PARTICLE_ITERATION)

        # get particle buffers
        posBuff = self.particleSystem.GetPositionBuffer()
        colorBuff = self.particleSystem.GetColorBuffer()
        count = self.particleSystem.GetParticleCount()
        radius = self.particleSystem.GetRadius()

        # important: pass posBuff.this and colorBuff.this as SwigPyObject (parsable at C++)
        self.particle = core.particle(
            posBuff.this, colorBuff.this, count, radius)
        showcase.add(self.particle)

    def update(self):
        self.boxF1.position = (
            self.body1.transform.position.x, self.body1.transform.position.y)
        self.boxF1.rotation = vmath.quat_rotationZ(self.body1.transform.angle)

        self.boxF2.position = (
            self.body2.transform.position.x, self.body2.transform.position.y)
        self.boxF2.rotation = vmath.quat_rotationZ(self.body2.transform.angle)

    def MouseDown(self, p):
        self.mouseWorld = p
        self.mouseTracing = True
        self.mouseTracerPosition = p
        self.mouseTracerVelocity = Box2D.b2Vec2(0.0, 0.0)

        if self.mouseJoint:
            return

        aabb = Box2D.b2AABB(lowerBound=p - (0.001, 0.001),
                            upperBound=p + (0.001, 0.001))

        query = QueryCallback(p)
        self.world.QueryAABB(query, aabb)

        if query.fixture:
            body = query.fixture.body
            self.mouseJoint = self.world.CreateMouseJoint(
                bodyA=self.ground,
                bodyB=body,
                target=p,
                maxForce=100.0 * body.mass)
            body.awake = True

    def MouseUp(self, p):
        if self.mouseJoint:
            self.world.DestroyJoint(self.mouseJoint)
            self.mouseJoint = None

    def MouseMove(self, p):
        self.mouseWorld = p
        if self.mouseJoint:
            self.mouseJoint.target = p

    def ConvertScreenToWorld(self, scrx, scry, worldz, cam):
        invproj = vmath.inverse(cam.projectionMatrix)
        invview = cam.viewInverseMatrix

        w, h = core.viewSize()
        x = scrx / w * 2
        y = scry / h * 2

        pos = vmath.vec4(x, y, 0.0, 1.0)
        npos = invproj * pos
        npos = invview * npos
        npos.z /= npos.w
        npos.x /= npos.w
        npos.y /= npos.w
        npos.w = 1.0

        pos = vmath.vec4(x, y, 1.0, 1.0)
        fpos = invproj * pos
        fpos = invview * fpos
        fpos.z /= fpos.w
        fpos.x /= fpos.w
        fpos.y /= fpos.w
        fpos.w = 1.0

        dir = vmath.normalize(fpos - npos)
        return npos + (dir * (npos.z - worldz))

    def handleTouch(self, touch):
        if touch:
            cur_x = touch['cur_x']
            cur_y = touch['cur_y']
            _pos = self.ConvertScreenToWorld(cur_x, cur_y, 0, self.cam)

            pos = Box2D.b2Vec2(_pos.x / self.cam.screenScale.x,
                               _pos.y / self.cam.screenScale.y)
            if touch['is_pressed']:
                self.MouseDown(pos)
            elif touch['is_released']:
                self.MouseUp(pos)
            elif touch['is_moved']:
                self.MouseMove(pos)
