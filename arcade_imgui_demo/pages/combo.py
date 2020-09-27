import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Combo(Page):
    def reset(self):
        self.current = 2

    def render(self):
        imgui.begin("Example: combo widget")

        clicked, self.current = imgui.combo(
            "combo", self.current, ["first", "second", "third"]
        )

        imgui.end()

def install(app):
    app.add_page(Combo, "combo", "Combo")
