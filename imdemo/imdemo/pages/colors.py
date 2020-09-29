import arcade
import imgui
import imgui.core

from imdemo.page import Page


class ColorsPage(Page):
    def draw(self):
        style = imgui.get_style()
        
        imgui.begin("Colors")
        imgui.columns(4)
        for color in range(0, imgui.COLOR_COUNT):
            imgui.text("Color: {}".format(color))
            imgui.color_button("color#{}".format(color), *style.colors[color])
            imgui.next_column()

        imgui.end()

def install(app):
    app.add_page(ColorsPage, "colors", "Colors")
