
import igeCore as core
from igeCore.apputil import graphicsHelper
import igeVmath as vmath
import cv2

core.window(True, 480, 640)

showcase = core.showcase("case01")

cam = core.camera('maincam')
cam.position = vmath.vec3(0, 0, 1.5)

capture = cv2.VideoCapture(0)
width = capture.get(3)  # width
height = capture.get(4)  # height

tex = core.texture("photo", int(width), int(height))   #RGB format
efig = graphicsHelper.createSprite(width*0.001, height*0.001, tex)
efig.position = vmath.vec3(-0.15, 0.3, 0)
showcase.add(efig)

while(True):
    ret, frame = capture.read()
    frame = cv2.flip(frame,-1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    tex.setImage(frame)
    cam.shoot(showcase)
    core.swap()

capture.release()
