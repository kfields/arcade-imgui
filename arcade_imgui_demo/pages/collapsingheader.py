import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class CollapsingHeader(Page):
    def __init__(self, window):
        super().__init__(window, "collapsingheader", "Collapsing Header")
        self.visible = True

    def on_render(self):
        imgui.begin("Example: collapsing header")
        expanded, self.visible = imgui.collapsing_header("Expand me!", self.visible)

        if expanded:
            imgui.text("Now you see me!")
        imgui.end()

def install(app):
    app.add_page(CollapsingHeader(app))
