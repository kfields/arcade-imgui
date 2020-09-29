import arcade
import imgui
import imgui.core

from imdemo.page import Page


class Tooltip(Page):
    def draw(self):
        imgui.begin("Example: tooltip")
        imgui.button("Click me!")
        if imgui.is_item_hovered():
            imgui.begin_tooltip()
            imgui.text("This button is clickable.")
            imgui.text("This button has full window tooltip.")
            texture_id = imgui.get_io().fonts.texture_id
            imgui.image(texture_id, 512, 64, border_color=(1, 0, 0, 1))
            imgui.end_tooltip()
        imgui.end()

def install(app):
    app.add_page(Tooltip, "tooltip", "Tooltip")
