import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Index(Page):
    def __init__(self, window):
        super().__init__(window, "index", "Index")
        self.current = 0

    def on_render(self):
        imgui.begin("Index")

        imgui.text("Welcome to the Arcade ImGui Demo!")
        
        imgui.end()

def install(app):
    app.add_page(Index(app))