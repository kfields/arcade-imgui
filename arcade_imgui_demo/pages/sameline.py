import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class SameLinePage(Page):
    def render(self):
        imgui.begin("Example: same line widgets")

        imgui.text("same_line() with defaults:")
        imgui.button("yes"); imgui.same_line()
        imgui.button("no")

        imgui.text("same_line() with fixed position:")
        imgui.button("yes"); imgui.same_line(position=50)
        imgui.button("no")

        imgui.text("same_line() with spacing:")
        imgui.button("yes"); imgui.same_line(spacing=50)
        imgui.button("no")

        imgui.end()

def install(app):
    app.add_page(SameLinePage, "sameline", "Same Line")
