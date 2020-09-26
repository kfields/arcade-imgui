import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Bullet(Page):
    def __init__(self, window):
        super().__init__(window, "bullet", "Bullet")

    def on_render(self):
        imgui.begin("Example: bullets")

        for i in range(10):
            imgui.bullet()

        imgui.end()


class BulletText(Page):
    def __init__(self, window):
        super().__init__(window, "bullettext", "Bullet Text")

    def on_render(self):
        imgui.begin("Example: bullet text")
        imgui.bullet_text("Bullet 1")
        imgui.bullet_text("Bullet 2")
        imgui.bullet_text("Bullet 3")
        imgui.end()

def install(app):
    app.add_page(Bullet(app))
    app.add_page(BulletText(app))