import os

import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class ImageButton(Page):
    def __init__(self, window):
        super().__init__(window, "imagebutton", "Image Button")
        image_path = os.path.join('assets', 'robocute.png')
        self.texture = window.ctx.load_texture(image_path, flip=False)

    def on_render(self):
        imgui.begin("Image Button")
        imgui.image_button(self.texture.glo, *self.texture.size)
        imgui.end()

def install(app):
    app.add_page(ImageButton(app))
