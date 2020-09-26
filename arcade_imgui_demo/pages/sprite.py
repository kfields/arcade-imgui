import os

import OpenGL.GL as gl
import numpy as np

import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page

SPRITE_SCALING = 0.5

def load_texture_from_sprite(sprite):
    im = sprite.texture.image.convert("RGB")
    w, h = im.size
    imdata = np.frombuffer(im.tobytes(), np.uint8)
    texture_id = gl.glGenTextures(1)
    print(f"Sprite Texture ID: {texture_id}")
    gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)

    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT,1)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, w, h, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, imdata)

    return texture_id, w, h


class SpritePage(Page):
    def __init__(self, window):
        super().__init__(window, "sprite", "Sprite")
        self.sprite = arcade.Sprite(":resources:images/space_shooter/playerShip1_orange.png", SPRITE_SCALING)
        self.texture_id, self.width, self.height = load_texture_from_sprite(self.sprite)

    def on_render(self):
        imgui.begin("Sprite")
        imgui.image(self.texture_id, self.width, self.height)
        imgui.end()

def install(app):
    app.add_page(SpritePage(app))
