import os

import OpenGL.GL as gl
import numpy as np
from PIL import Image

import arcade
import imgui
import imgui.core

from arcade_imgui_demo.page import Page

def load_texture_from_file(filepath):
    im = Image.open(filepath).convert("RGB")
    w, h = im.size
    imdata = np.frombuffer(im.tobytes(), np.uint8)
    texname = gl.glGenTextures(1)
    print(f"Texture: {texname}")
    gl.glBindTexture(gl.GL_TEXTURE_2D, texname)

    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT,1)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, w, h, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, imdata)

    return texname, w, h


class ImagePage(Page):
    def __init__(self, window):
        super().__init__(window, "image", "Image")
        image_path = os.path.join('assets', 'robocute.png')
        self.texture_id, self.width, self.height = load_texture_from_file(image_path)

    def on_render(self):
        imgui.begin("Image example")
        imgui.image(self.texture_id, self.width, self.height)
        imgui.end()

def install(app):
    app.add_page(ImagePage(app))
