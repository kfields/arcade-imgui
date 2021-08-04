import arcade
import imgui
import imgui.core

from imdemo.page import Page


class Rect(Page):
    def draw(self):
        imgui.begin("Rectangle")
        draw_list = imgui.get_window_draw_list()
        p1 = self.rel(20, 35)
        p2 = self.rel(90, 80)
        draw_list.add_rect(*p1, *p2, imgui.get_color_u32_rgba(1,1,0,1), thickness=3)
        p1 = self.rel(110, 35)
        p2 = self.rel(180, 80)
        draw_list.add_rect(*p1, *p2, imgui.get_color_u32_rgba(1,0,0,1), rounding=5, thickness=3)
        imgui.end()

class RectFilled(Page):
    def draw(self):
        imgui.begin("Rectangle Filled")
        draw_list = imgui.get_window_draw_list()
        p1 = self.rel(20, 35)
        p2 = self.rel(90, 80)
        draw_list.add_rect_filled(*p1, *p2, imgui.get_color_u32_rgba(1,1,0,1))
        p1 = self.rel(110, 35)
        p2 = self.rel(180, 80)
        draw_list.add_rect_filled(*p1, *p2, imgui.get_color_u32_rgba(1,0,0,1), 5)
        imgui.end()

def install(app):
    app.add_page(Rect, "rect", "Rectangle")
    app.add_page(RectFilled, "rectfilled", "Rectangle Filled")
