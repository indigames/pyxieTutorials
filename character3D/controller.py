"""
indi game engine
Tutorial04

controller.py

Controller class
"""
import igeCore as core
import igeVmath as vmath
from igeCore.apputil import graphicsHelper


class Controller( ):
    def __init__(self):
        self.frame = graphicsHelper.createSprite(50,50,'images/ctrl01')
        self.button = graphicsHelper.createSprite(50,50,'images/ctrl02')

    def step(self):

        touch = core.singleTouch()
        if touch is not None:
            self.frame.position = vmath.vec3(touch['org_x'],touch['org_y'],0)
            self.button.position = vmath.vec3(touch['cur_x'],touch['cur_y'],10)
        else:
            self.frame.position = vmath.vec3(0,1000,0)
            self.button.position = vmath.vec3(0,1000,10)