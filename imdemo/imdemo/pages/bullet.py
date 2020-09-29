import arcade
import imgui
import imgui.core

from imdemo.page import Page


class Bullet(Page):
    def draw(self):
        imgui.begin(self.title)

        for i in range(10):
            imgui.bullet()

        imgui.end()


class BulletText(Page):
    def draw(self):
        imgui.begin(self.title)
        imgui.bullet_text("Bullet 1")
        imgui.bullet_text("Bullet 2")
        imgui.bullet_text("Bullet 3")
        imgui.end()

def install(app):
    app.add_page(Bullet, "bullet", "Bullets")
    app.add_page(BulletText,  "bullettext", "Bullets with Text")