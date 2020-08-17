"""
indi game engine
using Effekseer with ige
"""
import igeCore as core
from igeCore import apputil
import igeVmath as vmath
import imgui
from igeCore.apputil.imguirenderer import ImgiIGERenderer

# open or resize window (This function is valid only on PC,Ignored in smartphone apps)
core.window(True, 480, 640)
# core.window(True, 1280, 720)

imgui.create_context()

impl = ImgiIGERenderer()

import igeEffekseer

textures = {}
def f_texture_loader(name, type):
    print('f_texture_loader - ' + name)
    tex = core.texture(name)    
    textures[name] = tex
    return (tex.width, tex.height, tex.id, tex.numMips > 1)

_w, _h = core.deviceSize()

igeEffekseer.texture_loader(f_texture_loader)
_particle = igeEffekseer.particle()

_particle.camera_eye = (10.0, 5.0, -20.0)
_particle.camera_at = (0.0, 0.0, 0.0)
_particle.camera_up = (0.0, 1.0, 0.0)

_particle.projection_ortho = False
_particle.projection_viewsize = (_w / 10, _h / 10)

# _particle.projection_viewport = (_w, _h)
_particle.projection_near = 1.0
_particle.projection_far = 1000.0
_particle.projection_fov = 90.0

_particle.framerate = 60.0

_distortion_hd = -1
_laser_hd = -1
_homing_hd = -1
_tornade_hd = -1

_color = 1.0, 0.0, 1.0, 1.0

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
    
    imgui.begin("Effekseer", True)
    
    imgui.push_id('Particle')
    imgui.text('Particle')
    imgui.same_line()
    if imgui.button("Init") and _particle is None:
        _particle = igeEffekseer.particle()
    imgui.same_line()
    if imgui.button("Destroy"):
        del _particle
        _particle = None
    imgui.pop_id()
    
    if _particle is not None:
        imgui.text('drawcall:' + str(_particle.drawcall_count()) + ' vertex:' + str(_particle.vertex_count()))
        imgui.text('update:' + str(_particle.update_time()) + ' draw:' + str(_particle.draw_time()))
        
        imgui.push_id('Simple_Distortion')
        imgui.text('Distortion')
        imgui.same_line()
        if imgui.button("play"):
            _distortion_hd = _particle.add('Simple_Distortion.efk')
        imgui.same_line()    
        if imgui.button("move"):
            _particle.set_location(_distortion_hd, 0.0, -10.0, 0.0) 
        imgui.same_line()
        if imgui.button("pause?"):
            _particle.set_pause(_distortion_hd, not _particle.get_pause(_distortion_hd))
        imgui.same_line()
        if imgui.button("show?"):
            _particle.set_shown(_distortion_hd, not _particle.get_shown(_distortion_hd))
        imgui.same_line()    
        if imgui.button("stop"):
            _particle.remove(_distortion_hd)            
        _, _color = imgui.color_edit4("color", *_color, show_alpha=True)
        _particle.set_color(_distortion_hd, int(_color[0] * 255), int(_color[1] * 255), int(_color[2] * 255), int(_color[3] * 255))
        imgui.pop_id()
        
        imgui.push_id('Laser01')
        imgui.text('Laser01')
        imgui.same_line()
        if imgui.button("play"):
            _laser_hd = _particle.add('Laser01.efk', (0.0, 0.0, 0.0))
        imgui.same_line()    
        if imgui.button("stop"):
            _particle.remove(_laser_hd)          
        imgui.pop_id()
        
        imgui.push_id('Homing_Laser01')
        imgui.text('Homing_Laser01')
        imgui.same_line()
        if imgui.button("play"):
            _homing_hd = _particle.add('Homing_Laser01.efk', (0.0, -10.0, 0.0))
        imgui.same_line()    
        if imgui.button("stop"):
            _particle.remove(_homing_hd)
        imgui.pop_id()
        
        imgui.push_id('MagicTornade')
        imgui.text('MagicTornade')
        imgui.same_line()
        if imgui.button("play"):
            _tornade_hd = _particle.add('MagicTornade.efk')
        imgui.same_line()    
        if imgui.button("stop"):
            _particle.remove(_tornade_hd)
        imgui.pop_id()
        
        if imgui.button("Stop All"):
            _particle.stop_all_effects()  
    
    imgui.end()    
    imgui.render()
    impl.render(imgui.get_draw_data())
    
    if _particle is not None:
        _particle.shoot(core.getElapsedTime())
    
    core.swap()