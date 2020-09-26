import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Colors(Page):
    def __init__(self, window):
        super().__init__(window, "colors", "Colors")

    def on_render(self):
        style = imgui.get_style()
        imgui.begin("Colors")
        imgui.columns(4)
        for color in range(0, imgui.COLOR_COUNT):
            imgui.text("Color: {}".format(color))
            imgui.color_button("color#{}".format(color), *style.colors[color])
            imgui.next_column()

        imgui.end()

def install(app):
    app.add_page(Colors(app))
