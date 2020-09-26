import os
import arcade
import imgui
import imgui.core

import OpenGL.GL as gl
import numpy as np
from PIL import Image

from arcade_imgui import ArcadeRenderer

def load_texture_from_file(filepath):
    im = Image.open(filepath).convert("RGB")
    w, h = im.size
    imdata = np.frombuffer(im.tobytes(), np.uint8)
    texname = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texname)

    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT,1)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, w, h, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, imdata)

    return texname, w, h

class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        imgui.create_context()
        self.renderer = ArcadeRenderer(window)
        image_path = os.path.join('assets', 'robocute.png')
        self.texture_id, self.width, self.height = load_texture_from_file(image_path)

    def render(self):
        imgui.new_frame()

        imgui.set_next_window_position(16, 32, imgui.ONCE)
        imgui.set_next_window_size(512, 512, imgui.ONCE)

        imgui.begin("Image example")
        imgui.image(self.texture_id, self.width, self.height)
        imgui.end()

        imgui.end_frame()

        imgui.render()

        self.renderer.render(imgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Image Example", resizable=True)
        self.gui = MyGui(self)
        #
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)


    def on_draw(self):
        arcade.start_render()
        self.gui.render()


app = App()
arcade.run()
