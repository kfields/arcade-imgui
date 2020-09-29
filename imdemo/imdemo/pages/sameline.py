import arcade
import imgui
import imgui.core

from imdemo.page import Page


class SameLinePage(Page):
    def draw(self):
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
