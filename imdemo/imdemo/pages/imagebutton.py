import os
import random
import arcade
import imgui

from imdemo.page import Page

MESSAGES = [
    "Hey! That tickles!!!",
    "Cut it out!",
    "Wise guy.",
    "Oh no you didn't"
]

class ImageButton(Page):
    def __init__(self, window, name, title):
        super().__init__(window, name, title)
        image_path = window.resource_path / 'robocute.png'
        self.texture = window.ctx.load_texture(image_path, flip=False)
        self.message = ''

    def draw(self):
        imgui.begin("Image Button")
        if imgui.image_button(self.texture.glo, *self.texture.size):
            self.message = MESSAGES[random.randint(0, len(MESSAGES)-1)]
        imgui.text(self.message)
        imgui.end()

def install(app):
    app.add_page(ImageButton, "imagebutton", "Image Button")
