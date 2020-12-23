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

sfxr_preset = 0
sfxr_handle = -1
position_3d = 0.0, 0.0, 0.0

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
    igeSound.update()

    imgui.new_frame()

    if imgui.begin_main_menu_bar():
        if imgui.begin_menu("File", True):
            clicked_quit, selected_quit = imgui.menu_item("Quit", 'Cmd+Q', False, True)
            if clicked_quit:
                exit(1)
            imgui.end_menu()
        imgui.end_main_menu_bar()

    imgui.begin("Sound", True, imgui.WINDOW_ALWAYS_AUTO_RESIZE)
    
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
    
    imgui.separator()
    
    imgui.push_id('sfxr')
    imgui.text('sfxr + 3d')
    imgui.same_line()
    if imgui.button("play"):
        sfxr_handle = igeSound.play(sfxr_preset, is_3d=True, position=position_3d, loop=True)
    imgui.same_line()
    if imgui.button("stop"):
        igeSound.stop(sfxr_handle)
    _, sfxr_preset = imgui.slider_int("preset", sfxr_preset, min_value=0, max_value=6, format="%d")
    position_changed, position_3d = imgui.slider_float3("position", *position_3d, min_value=0, max_value=500, format="%.1f", power=1.0)
    if position_changed is True:
        igeSound.set3dSourcePosition(sfxr_handle, position_3d)
        igeSound.set3dAttenuation(sfxr_handle, igeSound.EXPONENTIAL_DISTANCE, 0.25)   
    imgui.pop_id()
    
    if imgui.button("Stop All"):
        igeSound.stopAll()
    
    imgui.end()

    imgui.render()
    impl.render(imgui.get_draw_data())
    core.swap()