"""
pyxie game engine
Tutorial01

star ship moves when you touch the screen
"""
import pyxie
from pyxie import devtool
from pyxie import apputil
import pyvmath as vmath
import os.path

# convert png to the format suitable for the platform (ship.png -> ship.pyxi)
# devtool module can not be used in the app
# this process should be completed in advance, not at runtime
if not os.path.exists('ship.pyxi'):
    devtool.convertTextureToPlatform('ship.png', 'ship', pyxie.TARGET_PLATFORM_PC, False, False)

# open or resize window (This function is valid only on PC,Ignored in smartphone apps)
pyxie.window(True, 480, 640)

# create drawable rectangle object
# apputil module is just a sample code
# please copy and edit it for your own convenience.
ship = apputil.createSprite(100, 100, "ship")

camera = pyxie.camera("cam01")
camera.orthographicProjection = True
camera.position = (0, 0, 100)

# what you want to draw should be registered in showcase
showcase = pyxie.showcase("case01")
showcase.add(ship)

l_rot = vmath.mat_rotation(-0.05, 2)
r_rot = vmath.mat_rotation(0.05, 2)

goal = vmath.vec2(0, 0)
pos = vmath.vec2(0, 0)
dir = vmath.vec2(0, 1)

loop = True
while loop:
    touch = pyxie.singleTouch()
    if touch is not None:
        goal = vmath.vec2(touch['cur_x'], touch['cur_y'])

    d = goal - pos
    dist = vmath.length(d)
    d = vmath.normalize(d)
    r = vmath.dot(d, dir)
    if r < 0.98:
        n = vmath.cross(d, dir)
        if n > 0:
            dir = l_rot * dir
        else:
            dir = r_rot * dir
    if dist > 5.0:
        pos = pos + dir

    # update the direction and position of the ship object
    ship.rotation = vmath.normalize(vmath.quat_rotation((0, 1), dir))
    ship.position = pos

    # render the objects contained in showcase from the camera.
    camera.shoot(showcase)

    # update frame buffer
    pyxie.swap()
