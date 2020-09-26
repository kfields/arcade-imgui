import os

import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page


class ImageDraw(Page):
    def __init__(self, window):
        super().__init__(window, "imagedraw", "Image Draw")
        image_path = os.path.join('assets', 'robocute.png')
        self.texture = window.ctx.load_texture(image_path, flip=False)

    def on_render(self):
        imgui.begin("Image example")
        draw_list = imgui.get_window_draw_list()
        draw_list.add_image(self.texture.glo, (0, 0), self.texture.size)
        imgui.end()

def install(app):
    app.add_page(ImageDraw(app))
