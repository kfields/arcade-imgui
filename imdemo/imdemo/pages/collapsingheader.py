import arcade
import imgui
import imgui.core

from imdemo.page import Page


class CollapsingHeader(Page):
    def reset(self):
        self.visible = True

    def draw(self):
        imgui.begin("Example: collapsing header")
        expanded, self.visible = imgui.collapsing_header("Expand me!", self.visible)

        if expanded:
            imgui.text("Now you see me!")
        imgui.end()

def install(app):
    app.add_page(CollapsingHeader, "collapsingheader", "Collapsing Header")
