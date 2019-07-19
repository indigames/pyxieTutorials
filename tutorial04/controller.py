"""
pyxie game engine
Tutorial04

controller.py

Controller class
"""
import pyxie
import pyvmath as vmath
from pyxie.apputil import graphicsHelper


class Controller():
    def __init__(self):
        self.frame = graphicsHelper.createSprite(50,50,'images/ctrl01')
        self.button = graphicsHelper.createSprite(50,50,'images/ctrl02')
        self.camera = pyxie.camera('2dcam')
        self.camera.orthographicProjection = True
        self.camera.position = (0, 0, 100)
        self.showcase = pyxie.showcase('2dcase')
        self.showcase.add(self.frame)
        self.showcase.add(self.button)

    def step(self):

        touch = pyxie.singleTouch()
        if touch is not None:
            self.frame.position = vmath.vec3(touch['org_x'],touch['org_y'],0)
            self.button.position = vmath.vec3(touch['cur_x'],touch['cur_y'],1)
            self.camera.shoot(self.showcase)
           