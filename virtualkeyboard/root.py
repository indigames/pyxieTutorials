"""
indi game engine
using virtual keyboard with ige
"""
import igeCore as core
from igeCore import apputil
import igeVmath as vmath
import imgui
from igeCore.apputil.imguirenderer import ImgiIGERenderer


# open or resize window (This function is valid only on PC,Ignored in smartphone apps)
core.window(True, 480, 640)

imgui.create_context()

impl = ImgiIGERenderer()

while True:
    w, h = core.viewSize()
    curX = 0
    curY = 0
    press = 0
    touch = core.singleTouch()
    if touch != None:
        curX = touch['cur_x'] + w // 2
        curY = -touch['cur_y'] + h // 2
        press = touch['is_holded'] | touch['is_moved']
    impl.process_inputs()

    core.update()

    imgui.new_frame()

    if imgui.begin_main_menu_bar():
        if imgui.begin_menu("File", True):
            clicked_quit, selected_quit = imgui.menu_item("Quit", 'Cmd+Q', False, True)
            if clicked_quit:
                exit(1)
            imgui.end_menu()
        imgui.end_main_menu_bar()

    imgui.begin("Custom window", True)
    imgui.text("Virtual Keyboard : " + str(core.isVirtualKeyboardShown()))
    imgui.text("Value: " + core.getInputText())
    if imgui.button("Show Virtual Keyboard"):
        core.showVirtualKeyboard()
    if imgui.button("Hide Virtual Keyboard"):
        core.hideVirtualKeyboard()
    
    imgui.end()

    imgui.render()
    impl.render(imgui.get_draw_data())
    core.swap()
