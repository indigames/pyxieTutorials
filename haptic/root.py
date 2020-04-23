"""
indi game engine
Tutorial02

using imgui with indi
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

haptic = core.haptic()
haptic.init()
ct = 0
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

    imgui.new_frame()

    imgui.begin("Custom window", True)
    if imgui.button("HAPTIC_SELECTION"):
        haptic.play(core.HAPTIC_SELECTION, -1)
    if imgui.button("HAPTIC_SUCCESS"):
        haptic.play(core.HAPTIC_SUCCESS, -1)
    if imgui.button("HAPTIC_WARNING"):
        haptic.play(core.HAPTIC_WARNING, -1)
    if imgui.button("HAPTIC_FAILURE"):
        haptic.play(core.HAPTIC_FAILURE, -1)
    if imgui.button("HAPTIC_LIGHT_IMPACT"):
        haptic.play(core.HAPTIC_LIGHT_IMPACT, -1)
    if imgui.button("HAPTIC_MEDIUM_IMPACT"):
        haptic.play(core.HAPTIC_MEDIUM_IMPACT, -1)
    if imgui.button("HAPTIC_HEAVY_IMPACT"):
        haptic.play(core.HAPTIC_HEAVY_IMPACT, -1)
    imgui.end()

    ct += 1
    if ct == 2:
        haptic.play(core.HAPTIC_HEAVY_IMPACT, -1)
        ct = 0

    imgui.render()
    impl.render(imgui.get_draw_data())
    core.swap()
