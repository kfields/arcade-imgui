import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Empty(Page):
    def __init__(self, window):
        super().__init__(window, "child", "Child")

    def on_render(self):
        imgui.begin("Example: empty window")
        imgui.end()

def install(app):
    app.add_page(Empty(app))
