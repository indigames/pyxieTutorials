"""
pyxie game engine
Tutorial03

using Box2D with pyxie
"""

import pyxie
import pyvmath as vmath
import Box2D
from Box2D.b2 import (world, polygonShape, staticBody, dynamicBody)
from DynamicBox import DynamicBox


# open or resize window (This function is valid only on PC,Ignored in smartphone apps)
pyxie.window(True, 480, 640)

cam = pyxie.camera("maincam")
cam.orthographicProjection = True
cam.position = vmath.vec3(0.0, 0.0, 100.0)

showcase = pyxie.showcase()

boxes = []

PPM = 20.0  # pixels per meter
TARGET_FPS = 60
TIME_STEP = 1.0 / TARGET_FPS

world = world(gravity=(0, -10), doSleep=True)
boxes.append(DynamicBox(world, showcase, (0, -100), (150, 20), 0, True))
boxes.append(DynamicBox(world, showcase, (10, 100), (10, 5), 15))

while True:
    touch = pyxie.singleTouch()
    if touch is not None and touch['is_pressed']:
        boxes.append(DynamicBox(world, showcase, (touch['cur_x'], touch['cur_y']), (10, 5), 15))

    world.Step(TIME_STEP, 10, 10)
    for box in boxes:
        box.update()
    cam.shoot(showcase)
    pyxie.swap()
