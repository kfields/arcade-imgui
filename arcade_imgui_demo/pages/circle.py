import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Circle(Page):
    def __init__(self, window):
        super().__init__(window, "circle", "Circle")

    def on_render(self):
        imgui.begin("Circle")
        draw_list = imgui.get_window_draw_list()
        draw_list.add_circle(100, 60, 30, imgui.get_color_u32_rgba(1,1,0,1), thickness=3)
        imgui.end()

class CircleFilled(Page):
    def __init__(self, window):
        super().__init__(window, "circlefilled", "Filled Circle")

    def on_render(self):
        imgui.begin("Filled")
        draw_list = imgui.get_window_draw_list()
        draw_list.add_circle_filled(100, 60, 30, imgui.get_color_u32_rgba(1,1,0,1))
        imgui.end()

def install(app):
    app.add_page(Circle(app))
    app.add_page(CircleFilled(app))


