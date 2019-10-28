
import pyxie
from pyxie.apputil import graphicsHelper
import pyvmath as vmath
import cv2

pyxie.window(True, 480, 640)

showcase = pyxie.showcase("case01")

cam = pyxie.camera('maincam')
cam.position = vmath.vec3(0, 0, 1.5)

capture = cv2.VideoCapture(0)
width = capture.get(3)  # width
height = capture.get(4)  # height

tex = pyxie.texture("photo", int(width), int(height))   #RGB format
efig = graphicsHelper.createSprite(width*0.001, height*0.001, tex)
efig.position = vmath.vec3(-0.15, 0.3, 0)
showcase.add(efig)

while(True):
    ret, frame = capture.read()
    frame = cv2.flip(frame,-1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    tex.setImage(frame)
    cam.shoot(showcase)
    pyxie.swap()

capture.release()
