import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Rect(Page):
    def render(self):
        imgui.begin("Rectangle")
        draw_list = imgui.get_window_draw_list()
        draw_list.add_rect(20, 35, 90, 80, imgui.get_color_u32_rgba(1,1,0,1), thickness=3)
        draw_list.add_rect(110, 35, 180, 80, imgui.get_color_u32_rgba(1,0,0,1), rounding=5, thickness=3)
        imgui.end()

class RectFilled(Page):
    def render(self):
        imgui.begin("Rectangle Filled")
        draw_list = imgui.get_window_draw_list()
        draw_list.add_rect_filled(20, 35, 90, 80, imgui.get_color_u32_rgba(1,1,0,1))
        draw_list.add_rect_filled(110, 35, 180, 80, imgui.get_color_u32_rgba(1,0,0,1), 5)
        imgui.end()

def install(app):
    app.add_page(Rect, "rect", "Rectangle")
    app.add_page(RectFilled, "rectfilled", "Rectangle Filled")
