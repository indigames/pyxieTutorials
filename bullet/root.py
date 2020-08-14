import igeCore as core
import igeBullet
import imgui
from igeCore.apputil.imguirenderer import ImgiIGERenderer
from utils import Utils
from rigidbody import Rigidbody
from ragdoll import Ragdoll
from hinge import Hinge
from conetwist import ConeTwist
from vehicle import Vehicle
from compound import Compound
from meshshape import Meshshape

core.window(True, 480, 640)

def imguiUpdate(select):
    impl.process_inputs()
    imgui.new_frame()
    imgui.begin("Custom window", True)
    clicked, select = imgui.listbox("Samples", select, samples, 10)
    imgui.end()
    imgui.render()
    impl.render(imgui.get_draw_data(), False)
    return clicked, select

imgui.create_context()
impl = ImgiIGERenderer()
samples = ['rigidbody', 'ragdoll', 'hinge', 'conetwist', 'compound', 'vehicle', 'meshShape']

case = core.showcase()
case.add(Utils().GetFigure())
camera = core.camera("cam01")
camera.position = (-30, 30, -30)
world = igeBullet.world()
world.gravity = (0,-10,0)
select = -1
demo = None

# case.add(core.figure('ground'))
# case.add(core.figure('shape'))
        
while True:
    core.update()
    world.step()
    camera.shoot(case)

    # if demo is not None:
        # demo.update()

    clicked, newselect = imguiUpdate(select)
    if clicked and newselect != select:
        select = newselect
        if select is 0:
            demo = Rigidbody()
        elif select is 1:
            demo = Ragdoll()
        elif select is 2:
            demo = Hinge()
        elif select is 3:
            demo = ConeTwist()
        elif select is 4:
            demo = Compound()
        elif select is 5:
            demo = Vehicle()
        elif select is 6:
            demo = Meshshape()
        demo.setup(world)

    core.swap()
