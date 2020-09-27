import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Index(Page):
    def render(self):
        imgui.begin("Index")

        imgui.text("Welcome to the Arcade ImGui Demo!")
        
        imgui.end()

def install(app):
    app.add_page(Index, "index", "Index")