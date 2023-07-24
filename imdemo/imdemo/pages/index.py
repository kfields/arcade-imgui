import imgui

from imdemo.page import Page


class Index(Page):
    def draw(self):
        imgui.begin("Index")

        imgui.text("Welcome to the Arcade ImGui Demo!")

        imgui.end()


def install(app):
    app.add_page(Index, "index", "Index")
