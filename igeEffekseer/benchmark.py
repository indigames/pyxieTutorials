"""
indi game engine
using Effekseer with ige
"""
import igeCore as core
from igeCore import apputil
import igeVmath as vmath
import imgui
from igeCore.apputil.imguirenderer import ImgiIGERenderer
import igeEffekseer
import os
import random

# open or resize window (This function is valid only on PC,Ignored in smartphone apps)
core.window(True, 480, 640)

imgui.create_context()
impl = ImgiIGERenderer()

textures = {}
def f_texture_loader(name, type):    
    tex = core.texture(name)    
    textures[name] = tex
    print('f_texture_loader - ' + name + ' => ' + str(tex.id))
    return (tex.width, tex.height, tex.id, tex.numMips > 1)

igeEffekseer.texture_loader(f_texture_loader)

effect_list = []
for root, dirs, files in os.walk("Effects"):
    for file in files:
        if file.endswith(".efk"):
            effect_list.append(os.path.join(root, file))

effect_current = 5

_particle_nb = 1000
_particle = igeEffekseer.particle(True)
_rotation = 0.0, 0.0, 0.0
_position = 0.0, -2.0, 0.0
_scale = .25, .25, .25
_dynamic = 1.0, 0.0, 0.0, 0.0
_particle.framerate = 60.0
_show_enabled = True
_loop_enabled = True
_benchmark_enabled = True
_update_enabled = True
_render_enabled = True
_culling_enabled = True

_handle = -1

_w, _h = core.deviceSize()

_position_range = -10.0, 10.0
_culling_size = 1.0

for seq in range(_particle_nb):
    _handle = _particle.add(effect_list[effect_current], loop=_loop_enabled)
    _particle.set_dynamic_input(_handle, _dynamic)
    _particle.set_location(_handle, random.uniform(*_position_range), random.uniform(*_position_range), _position[2])
    _particle.set_scale(_handle, _scale[0], _scale[1], _scale[2])

showcase = core.showcase("showcase")
camera = core.camera("cam01")
camera.position = (10, 5, 10)

figure = core.figure('Sapphiart/Sapphiart')
figure.position = _position
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
        _particle.shoot(camera.projectionMatrix, vmath.inverse(camera.viewInverseMatrix), core.getElapsedTime(), update=_update_enabled, render=_render_enabled, culling=_culling_enabled)
    
    imgui.new_frame()    
    imgui.begin("Effekseer", True, imgui.WINDOW_ALWAYS_AUTO_RESIZE)
    
    changed, effect_current = imgui.combo("Effects", effect_current, effect_list)
    if changed is True:
        _particle.stop_all_effects()
        for seq in range(_particle_nb):
            _handle = _particle.add(effect_list[effect_current], loop=_loop_enabled)  
            _particle.set_dynamic_input(_handle, _dynamic)
            _particle.set_location(_handle, random.uniform(*_position_range), random.uniform(*_position_range), _position[2])
            _particle.set_scale(_handle, _scale[0], _scale[1], _scale[2])
    
    if _particle is not None:
        imgui.text('instance:' + str(_particle.instance_count(_handle)) + ' total:' + str(_particle.total_instance_count()))
        imgui.text('DC=' + str(_particle.drawcall_count()) + ' VERT=' + str(_particle.vertex_count()))
        imgui.text('update=' + str(_particle.update_time()) + ' draw=' + str(_particle.draw_time()) + ' fps=' + str( int(1.0 / core.getElapsedTime())))
    
    _, _update_enabled = imgui.checkbox("Update", _update_enabled)
    imgui.same_line()
    _, _render_enabled = imgui.checkbox("Render", _render_enabled)
    imgui.same_line()
    _, _culling_enabled = imgui.checkbox("Culling", _culling_enabled)
    imgui.same_line()
    if imgui.button("Add"):
        for seq in range(_particle_nb):
            _handle = _particle.add(effect_list[effect_current], loop=_loop_enabled)  
            _particle.set_dynamic_input(_handle, _dynamic)
            _particle.set_location(_handle, random.uniform(-10.0, 10.0), random.uniform(-10.0, 10.0), _position[2])
            _particle.set_scale(_handle, _scale[0], _scale[1], _scale[2])
    
    if _benchmark_enabled is True:
        _, _particle_nb = imgui.slider_int("Number", _particle_nb, min_value=1, max_value=500,format="%d")

    changed, _position = imgui.slider_float3("Position", *_position, min_value=-10.0, max_value=10.0,format="%.0f", power=1)
    if changed is True:
        _particle.set_location(_handle, _position[0], _position[1], _position[2])
        
    changed, _rotation = imgui.slider_float3("Rotation", *_rotation, min_value=0.0, max_value=3.14 * 2,format="%.2f", power=1)
    if changed is True:
        _particle.set_rotation(_handle, _rotation[0], _rotation[1], _rotation[2])   
    
    changed, _scale = imgui.slider_float3("Scale", *_scale, min_value=0.0, max_value=2,format="%.2f", power=1)
    if changed is True:
        _particle.set_scale(_handle, _scale[0], _scale[1], _scale[2])
    
    changed, _dynamic = imgui.slider_float4("Dynamic_Input", *_dynamic, min_value=0.0, max_value=100.0,format="%.0f", power=1)
    if changed is True:
        _particle.set_dynamic_input(_handle, _dynamic) 
    
    imgui.end()    
    imgui.render()
    impl.render(imgui.get_draw_data(), clearColor=False)
    core.swap()