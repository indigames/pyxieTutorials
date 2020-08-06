"""
ige game launcher

root.py
"""
import igeCore as core
from igeCore import apputil
import igeVmath as vmath
import imgui
from igeCore.apputil.imguirenderer import ImgiIGERenderer
import igeSound

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

    imgui.begin("Sound", True)
    
    imgui.push_id('mp3')
    imgui.text('mp3')
    imgui.same_line()
    if imgui.button("play"):
        igeSound.play('sound/attack.mp3')
    imgui.same_line()    
    if imgui.button("stop"):
        igeSound.stop('sound/attack.mp3')    
    imgui.pop_id()
    
    imgui.push_id('wav')
    imgui.text('wav')
    imgui.same_line()
    if imgui.button("play"):
        igeSound.play('sound/spell.wav')
    imgui.same_line()    
    if imgui.button("stop"):
        igeSound.stop('sound/spell.wav')        
    imgui.pop_id()
    
    imgui.push_id('ogg')
    imgui.text('ogg')
    imgui.same_line()
    if imgui.button("play"):
        igeSound.play('sound/beep.ogg')
    imgui.same_line()    
    if imgui.button("stop"):
        igeSound.stop('sound/beep.ogg')
    imgui.pop_id()
    
    if imgui.button("Stop All"):
        igeSound.stopAll()
    
    imgui.end()

    imgui.render()
    impl.render(imgui.get_draw_data())
    core.swap()