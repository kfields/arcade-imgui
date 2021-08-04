import os

import arcade
import imgui
import imgui.core

from imdemo.page import Page


class ImageDraw(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        image_path = window.resource_path / 'robocute.png'
        self.texture = window.ctx.load_texture(image_path, flip=False)

    def draw(self):
        imgui.begin("Image Draw")
        draw_list = imgui.get_window_draw_list()
        pos = self.rel(0,0)
        pos2 = self.texture.size[0] + pos[0], self.texture.size[1] + pos[1]
        draw_list.add_image(self.texture.glo, pos, pos2)
        imgui.end()

def install(app):
    app.add_page(ImageDraw, "imagedraw", "Image Draw")
