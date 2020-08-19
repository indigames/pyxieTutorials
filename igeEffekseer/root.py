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

_particle.framerate = 60.0
_handle = _particle.add('Effects/MagicTornade.efk')
_particle.set_scale(_handle, 0.25, 0.25, 0.25)

_rotation = 0.0, 0.0, 0.0
_position = 0.0, 0.0, 0.0

_distortion_hd = -1
_laser_hd = -1
_homing_hd = -1
_tornade_hd = -1

_color = 1.0, 0.0, 1.0, 1.0

showcase = core.showcase("showcase")
camera = core.camera("cam01")
# camera.orthographicProjection = True

__w, __h = core.viewSize()

camera.orthoHeight = __h / 50
camera.position = (0, 0, 10)

figure = core.figure('Sapphiart/Sapphiart')
showcase.add(figure)

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
    
    camera.shoot(showcase)
    if _particle is not None:
        _particle.shoot(camera.projectionMatrix, vmath.inverse(camera.viewInverseMatrix), core.getElapsedTime())
    
    imgui.new_frame()    
    imgui.begin("Effekseer", True)
    
    changed, _rotation = imgui.slider_float3("Rotation", *_rotation, min_value=0.0, max_value=3.14 * 2,format="%.2f", power=1)
    if changed is True:
        _particle.set_rotation(_handle, _rotation[0], _rotation[1], _rotation[2])    

    position_changed, _position = imgui.slider_float3("Position", *_position, min_value=-10.0, max_value=10.0,format="%.0f", power=1)
    if position_changed is True:
        _particle.set_location(_handle, _position[0], _position[1], _position[2])   
    
    imgui.end()    
    imgui.render()
    impl.render(imgui.get_draw_data(), clearColor=False)
    core.swap()