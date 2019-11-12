"""
pyxie game engine
Tutorial03

using Box2D with pyxie
"""

import pyxie
import pyvmath as vmath
import Box2D

import Defines as DEF
from Bowl import Bowl

# open or resize window (This function is valid only on PC,Ignored in smartphone apps)
pyxie.window(True, DEF.SCREEN_WIDTH, DEF.SCREEN_HEIGHT)

# init opengl
pyxie.swap()

# camera
cam = pyxie.camera("maincam")
cam.orthographicProjection = True
cam.position = vmath.vec3(0.0, 0.0, 1.0)
cam.screenScale = vmath.vec2(DEF.SCREEN_SCALE, DEF.SCREEN_SCALE)

# showcases
showcase = pyxie.showcase()

# world
world = Box2D.b2World(gravity=(0, -DEF.GRAVITY), doSleep=True)

# objects
objects = []
bowl = Bowl(world, showcase, cam, (100, 100))
objects.append(bowl)

while True:
    touch = pyxie.singleTouch()
    bowl.handleTouch(touch)

    world.Step(DEF.TIME_STEP, DEF.VELOCITY_ITERATION,
               DEF.POSITION_ITERATION, DEF.PARTICLE_ITERATION)

    for obj in objects:
        obj.update()

    cam.shoot(showcase)
    pyxie.swap()
