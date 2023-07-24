import arcade
import imgui
import imgui.core

from imdemo.page import Page


class Overlay(Page):
    def draw(self):
        imgui.begin("Poly Line Overlay")
        draw_list = imgui.get_overlay_draw_list()
        draw_list.add_polyline([(20, 35), (90, 35), (55, 80)], imgui.get_color_u32_rgba(1,1,0,1), thickness=3)
        draw_list.add_polyline([(110, 35), (180, 35), (145, 80)], imgui.get_color_u32_rgba(1,0,0,1), flags=imgui.DRAW_CLOSED, thickness=3)
        imgui.end()

def install(app):
    app.add_page(Overlay, "overlay", "Overlay")
