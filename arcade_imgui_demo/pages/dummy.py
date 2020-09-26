import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Dummy(Page):
    def __init__(self, window):
        super().__init__(window, "dummy", "Dummy")

    def on_render(self):
        imgui.begin("Example: dummy elements")

        imgui.text("Some text with bullets:")
        imgui.bullet_text("Bullet A")
        imgui.bullet_text("Bullet B")

        imgui.dummy(0, 50)
        imgui.bullet_text("Text after dummy")

        imgui.end()

def install(app):
    app.add_page(Dummy(app))
