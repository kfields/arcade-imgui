from pathlib import Path

import arcade
import imgui
import imgui.core

from arcade_imgui import ArcadeRenderer

RESOURCE_PATH = Path(__file__).parent.parent / 'assets'

class MyGui:
    def __init__(self, window):
        self.window = window
        # Must create or set the context before instantiating the renderer
        imgui.create_context()
        self.renderer = ArcadeRenderer(window)

        io = imgui.get_io()
        self.new_font = io.fonts.add_font_from_file_ttf(str(RESOURCE_PATH / "DroidSans.ttf"), 20)
        self.renderer.refresh_font_texture()

    def draw(self):
        imgui.new_frame()

        imgui.begin("Font")

        imgui.text("Text displayed using default font")
        with imgui.font(self.new_font):
            imgui.text("Text displayed using custom font")

        imgui.end()

        imgui.end_frame()

        imgui.render()

        self.renderer.render(imgui.get_draw_data())


class App(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Font Image Example", resizable=True)
        self.gui = MyGui(self)

    def on_draw(self):
        arcade.start_render()
        self.gui.draw()


app = App()
arcade.run()
