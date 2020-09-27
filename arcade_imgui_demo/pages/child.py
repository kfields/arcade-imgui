import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Child(Page):
    def __init__(self, window):
        super().__init__(window, "child", "Child")

    def on_render(self):
        imgui.begin("Example: child region")

        imgui.begin_child("region", 150, -50, border=True)
        imgui.text("inside region")
        imgui.end_child()

        imgui.text("outside region")
        imgui.end()

def install(app):
    app.add_page(Child(app))
