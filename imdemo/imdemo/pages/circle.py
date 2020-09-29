import arcade
import imgui
import imgui.core

from imdemo.page import Page


class Circle(Page):
    def draw(self):
        imgui.begin("Circle")
        draw_list = imgui.get_window_draw_list()
        draw_list.add_circle(100, 60, 30, imgui.get_color_u32_rgba(1,1,0,1), thickness=3)
        imgui.end()

class CircleFilled(Page):
    def draw(self):
        imgui.begin("Filled")
        draw_list = imgui.get_window_draw_list()
        draw_list.add_circle_filled(100, 60, 30, imgui.get_color_u32_rgba(1,1,0,1))
        imgui.end()

def install(app):
    app.add_page(Circle, "circle", "Circle")
    app.add_page(CircleFilled, "circlefilled", "Filled Circle")


