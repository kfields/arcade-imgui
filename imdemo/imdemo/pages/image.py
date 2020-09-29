import os

import arcade
import imgui
import imgui.core

from imdemo.page import Page


class ImagePage(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        image_path = window.resource_path / 'robocute.png'
        self.texture = window.ctx.load_texture(image_path, flip=False)

    def draw(self):
        imgui.begin(self.title)
        imgui.image(self.texture.glo, *self.texture.size)
        imgui.end()

def install(app):
    app.add_page(ImagePage, "image", "Image")
