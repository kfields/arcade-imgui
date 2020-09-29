import arcade
import imgui
import imgui.core

from imdemo.page import Page


class Line(Page):
    def draw(self):
        imgui.begin("Line")
        draw_list = imgui.get_window_draw_list()
        draw_list.add_line(20, 35, 180, 80, imgui.get_color_u32_rgba(1,1,0,1), 3)
        draw_list.add_line(180, 35, 20, 80, imgui.get_color_u32_rgba(1,0,0,1), 3)
        imgui.end()

class PolyLine(Page):
    def draw(self):
        imgui.begin("Poly Line")
        draw_list = imgui.get_window_draw_list()
        draw_list.add_polyline([(20, 35), (90, 35), (55, 80)], imgui.get_color_u32_rgba(1,1,0,1), closed=False, thickness=3)
        draw_list.add_polyline([(110, 35), (180, 35), (145, 80)], imgui.get_color_u32_rgba(1,0,0,1), closed=True, thickness=3)
        imgui.end()

def install(app):
    app.add_page(Line, "line", "Line")
    app.add_page(PolyLine, "polyline", "Poly Line")
