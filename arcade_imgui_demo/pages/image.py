import os

import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class ImagePage(Page):
    def __init__(self, window):
        super().__init__(window, "image", "Image")
        image_path = os.path.join('assets', 'robocute.png')
        self.texture = window.ctx.load_texture(image_path, flip=False)

    def on_render(self):
        imgui.begin("Image example")
        imgui.image(self.texture.glo, *self.texture.size)
        imgui.end()

def install(app):
    app.add_page(ImagePage(app))
