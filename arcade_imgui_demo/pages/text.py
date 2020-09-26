import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class TextPage(Page):
    def __init__(self, window):
        super().__init__(window, "text", "Text")

    def on_render(self):
        imgui.begin("Text")
        draw_list = imgui.get_window_draw_list()
        draw_list.add_text(20, 35, imgui.get_color_u32_rgba(1,1,0,1), "Hello!")
        imgui.end()

def install(app):
    app.add_page(TextPage(app))
