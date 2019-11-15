import igeCore as core
from igeCore.apputil import graphicsHelper

core.window(True, 480, 640)

efig = graphicsHelper.textFigure("Hello World\nこんにちは世界", "ume-pgc5.ttf",32)

case = core.showcase()
case.add(efig)

camera = core.camera("cam01")
camera.orthographicProjection = True
camera.position = (0, 0, 100)


while True:
    camera.shoot(case)
    core.swap()
