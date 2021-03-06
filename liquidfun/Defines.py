import Box2D

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
SCREEN_SCALE = 4.0

# pixels per meter
PPM = 20.0
TARGET_FPS = 30
TIME_STEP = 1.0 / TARGET_FPS

GRAVITY = 9.8
VELOCITY_ITERATION = 8
POSITION_ITERATION = 3
PARTICLE_RADIUS = 0.15
PARTICLE_DENSITY = 1.0
PARTICLE_ITERATION = Box2D.b2CalculateParticleIterations(
    GRAVITY, PARTICLE_RADIUS, TIME_STEP)
