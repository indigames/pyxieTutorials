"""
pyxie game engine
Tutorial02

using imgui with pyxie
"""
import pyxie
from pyxie import apputil
import pyvmath as vmath
import imgui
from pyxie.apputil.imguirenderer import ImgiPyxieRenderer


# open or resize window (This function is valid only on PC,Ignored in smartphone apps)
pyxie.window(True, 480, 640)

imgui.create_context()

impl = ImgiPyxieRenderer()

while True:
    w, h = pyxie.viewSize()
    curX = 0
    curY = 0
    press = 0
    touch = pyxie.singleTouch()
    if touch != None:
        curX = touch['cur_x'] + w // 2
        curY = -touch['cur_y'] + h // 2
        press = touch['is_hold'] | touch['is_move']
    impl.process_inputs()

    imgui.new_frame()

    if imgui.begin_main_menu_bar():
        if imgui.begin_menu("File", True):
            clicked_quit, selected_quit = imgui.menu_item("Quit", 'Cmd+Q', False, True)
            if clicked_quit:
                exit(1)
            imgui.end_menu()
        imgui.end_main_menu_bar()

    imgui.show_test_window()

    imgui.begin("Custom window", True)
    imgui.text("Bar")
    imgui.text("w={}:h={}".format(w, h))
    imgui.text("x={}:y={}:press={}".format(curX, curY, press))
    imgui.text_colored("Eggs", 0.2, 1., 0.)
    imgui.end()

    imgui.render()
    impl.render(imgui.get_draw_data())
    pyxie.swap()
