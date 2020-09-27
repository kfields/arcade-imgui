import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class SeparatorPage(Page):
    def render(self):
        imgui.begin(self.title)

        imgui.text("Some text with bullets")
        imgui.bullet_text("Bullet A")
        imgui.bullet_text("Bullet A")

        imgui.separator()

        imgui.text("Another text with bullets")
        imgui.bullet_text("Bullet A")
        imgui.bullet_text("Bullet A")

        imgui.end()

def install(app):
    app.add_page(SeparatorPage, "separator", "Separator")
