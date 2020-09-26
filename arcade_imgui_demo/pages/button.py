import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class Button(Page):
    def __init__(self, window):
        super().__init__(window, "button", "Buttons")

    def on_render(self):
        imgui.begin("Example: buttons")

        imgui.button("Button 1")
        imgui.button("Button 2")

        imgui.end()

class ColorButton(Page):
    def __init__(self, window):
        super().__init__(window, "colorbutton", "Color Buttons")

    def on_render(self):
        imgui.begin("Example: color button")
        imgui.color_button("Button 1", 1, 0, 0, 1, 0, 10, 10)
        imgui.color_button("Button 2", 0, 1, 0, 1, 0, 10, 10)
        imgui.color_button("Wide Button", 0, 0, 1, 1, 0, 20, 10)
        imgui.color_button("Tall Button", 1, 0, 1, 1, 0, 10, 20)
        imgui.end()

def install(app):
    app.add_page(Button(app))
    app.add_page(ColorButton(app))
